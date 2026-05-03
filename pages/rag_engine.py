import os
from dotenv import load_dotenv
from pathlib import Path
from typing import List, Dict
from langchain_core.documents import Document
from langchain_community.document_loaders import PyPDFLoader, Docx2txtLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

from pages.prompts.chat_prompts import (
    LIGHT_MEDICAL_PROMPT,
    MEDICAL_RAG_PROMPT,
    CASUAL_LLM_PROMPT,
    FAREWELL_PROMPT,

    is_light_medical,
    is_serious_medical,
    is_medical_query,
    is_farewell,
    detect_language,
)

load_dotenv()

class HybridMedicalRAG:
    def __init__(self):
        self.model_name = os.getenv("MODEL_NAME", "openai/gpt-4o-mini")
        self.data_path = Path(os.getenv("DATA_PATH", "./data/raw"))
        self.db_path = Path(os.getenv("CHROMA_PATH", "./data/chroma_db"))

        if os.getenv("RESET_DB", "false") == "true":
            if self.db_path.exists():
                shutil.rmtree(self.db_path)
            
        api_key = os.getenv("OPENAI_API_KEY")

        if not api_key:
            raise ValueError("OPENAI_API_KEY not found")

        os.environ["OPENAI_API_KEY"] = api_key

        self.embeddings = OpenAIEmbeddings(
            model="text-embedding-3-small"
        )

        self.llm = ChatOpenAI(
            model=self.model_name,
            base_url="https://api.koboillm.com/v1",
            temperature=0,
        )
        self.vectorstore = self._load_or_build_vectorstore()
        
        # Chat history untuk context
        self.chat_history = []

    def clear_chat_history(self):
        """Clear chat history"""
        self.chat_history = []

    def get_stats(self):
        return {
            "has_vectorstore": self.vectorstore is not None,
            "chat_history_size": len(self.chat_history),
            "model": self.model_name,
            "sample_knowledge_size": self.vectorstore._collection.count() if self.vectorstore else 0
        }

    def process_document(self, file_path: str) -> bool:
        try:
            if file_path.endswith('.pdf'):
                loader = PyPDFLoader(file_path)
            elif file_path.endswith('.docx'):
                loader = Docx2txtLoader(file_path)
            elif file_path.endswith('.txt'):
                from langchain_community.document_loaders import TextLoader
                loader = TextLoader(file_path)
            else:
                return False
            
            docs = loader.load()
            splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=50)
            chunks = splitter.split_documents(docs)
            
            self.vectorstore.add_documents(chunks)
            return True
        except Exception as e:
            print(f"Error processing document: {e}")
            return False

    def load_documents(self) -> List[Document]:
        docs = []
        for file_path in self.data_path.glob("*"):
            if file_path.suffix.lower() == '.pdf':
                loader = PyPDFLoader(str(file_path))
                docs.extend(loader.load())
            elif file_path.suffix.lower() == '.docx':
                loader = Docx2txtLoader(str(file_path))
                docs.extend(loader.load())
        if not docs:
            docs = [
                Document(page_content="Batuk demam 3 hari: ISPA/pneumonia. Red flags: sesak napas.", metadata={"source": "sample"}),
                Document(page_content="Demam tinggi anak: infeksi serius. Red flags: lemas, kejang.", metadata={"source": "sample"}),
            ]
        return docs

    def _load_or_build_vectorstore(self) -> Chroma:
        if self.db_path.exists() and any(self.db_path.iterdir()):
            return Chroma(
                persist_directory=str(self.db_path),
                embedding_function=self.embeddings
            )
        else:
            docs = self.load_documents()
            splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
            chunks = splitter.split_documents(docs)
            return Chroma.from_documents(
                documents=chunks,
                embedding=self.embeddings,
                persist_directory=str(self.db_path)
            )
        
        
    def _is_query_relevant(self, query: str, threshold=0.5) -> bool:
        results = self.vectorstore.similarity_search(query, k=1)
        if not results:
            return False
        score = getattr(results[0], 'score', 1.0)
        return score >= threshold

    def _extract_text(self, response) -> str:
        if hasattr(response, 'content'):
            return response.content
        elif isinstance(response, dict) and 'text' in response:
            return response['text']
        else:
            return str(response)

    def _apply_language(self, prompt: str, lang: str) -> str:
        if lang == "English":
            return prompt + "\n\nAnswer in English."
        return prompt

    def query(self, user_query: str) -> Dict:
        self.chat_history.append({"role": "user", "content": user_query})
        
        history_context = "\n".join([
            f"{msg['role']}: {msg['content'][:100]}" 
            for msg in self.chat_history[-50:]
        ])

        # ✅ NEW: Check for farewell/thankyou FIRST
        if is_farewell(user_query):
            # Create farewell response
            prompt = ChatPromptTemplate.from_template(FAREWELL_PROMPT)
            chain = prompt | self.llm
            
            # Add context from chat history for personalization
            history_context = "\n".join([
                f"{msg['role']}: {msg['content'][:100]}" 
                for msg in self.chat_history[-50:]  # Last 3 messages
            ])
            
            response = chain.invoke({
                "history": history_context,
                "question": user_query,
            })
            
            answer_text = self._extract_text(response)
            self.chat_history.append({"role": "assistant", "content": answer_text})
            
            return {
                "answer": answer_text,
                "source": ["Farewell response"]
            }

        if self._is_query_relevant(user_query):
            docs = self.vectorstore.similarity_search(user_query, k=2)
            
            if not docs:
                return self._fallback_llm(user_query)
            
            context_text = "\n\n".join([doc.page_content[:300] for doc in docs])
            
            # Select prompt based on query type
            if is_serious_medical(user_query):
                prompt_template_str = MEDICAL_RAG_PROMPT
            elif is_light_medical(user_query):
                prompt_template_str = LIGHT_MEDICAL_PROMPT
            elif is_medical_query(user_query):
                prompt_template_str = MEDICAL_RAG_PROMPT
            else:
                prompt_template_str = CASUAL_LLM_PROMPT  # Fallback ke Ollama AI
            
            # Detect language and apply (clean - using _apply_language)
            lang = detect_language(user_query)
            prompt_template_str = self._apply_language(prompt_template_str, lang)
            
            # Create chain properly
            prompt = ChatPromptTemplate.from_template(prompt_template_str)
            chain = prompt | self.llm
            
            response = chain.invoke({
                "history": history_context,
                "question": user_query,
                "context": context_text,
            })
            
            answer_text = self._extract_text(response)
            
            self.chat_history.append({"role": "assistant", "content": answer_text})
            
            return {
                "answer": answer_text,
                "source": [doc.metadata.get("source", "PDF data") for doc in docs]
            }
        else:
            return self._fallback_llm(user_query)
        
    def _fallback_llm(self, user_query: str) -> Dict:
        """Fallback ke LLM langsung tanpa RAG context"""
        history_text = "\n".join([
            f"{msg['role']}: {msg['content']}" 
            for msg in self.chat_history[-5:]
        ])
        
        casual_prompt = CASUAL_LLM_PROMPT.format(
            history=history_text,
            question=user_query
        )
        
        response = self.llm.invoke(casual_prompt)
        answer_text = self._extract_text(response)
        
        self.chat_history.append({"role": "assistant", "content": answer_text})
        
        return {
            "answer": answer_text,
            "source": ["Ollama LLM - fallback"]
        }
