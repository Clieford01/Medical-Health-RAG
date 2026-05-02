"""
Chat prompts untuk hybrid medical chatbot
Enhanced version with better conflict resolution
"""
# ========================================================================
#                 Bagian ator kata-kata tleh cees
# ========================================================================

# KATA-KATA Gaul ini cees versi INDO
SLANG_INDO = [
    'bro', 'gue', 'lu', 'nih', 'gitu', 'banget', 'ya kan', 'loh', 
    'wkwk', 'mantap', 'keren', 'asik', 'sip', 'oke', 'mah', 'sip bro', 
    'sip gan', 'sip cuy', 'sip bos', 'siap gan', 'sip deh', 'oke deh', 
    'oke bro', 'woles', 'santai', 'gampang', 'gak masalah', 'gapapa', 
    'gak apa-apa', 'gak usah khawatir', 'tenang aja', 'santai aja', 
    'udah lah', 'udah deh', 'udah bro', 'udah cuy', 'udah', 'dong', 
    'kan', 'tuh', 'deh', 'mah', 'sih', 'dong', 'yaudah', 'yaudahlah'
]

# SLANG casual keywords versi ENGLISH
SLANG_ENG = [
    'bro', 'dude', 'yo', 'chill', 'lit', 'vibe', 'fam', 'sick', 'sup', 
    'homie', 'brodah', 'dawg', 'mate', 'buddy', 'amigo', 'all good', 
    'no worries', 'i got you', 'what up', 'sounds good', 'cool', 
    'awesome', 'nice', 'sweet', 'dope', 'rad', 'gnarly', 'wicked',
    "that's sick", "that's fire", 'oh yeah', 'oh really', 'for real', 
    'no way', 'you know it', 'yeah sure', 'totally', 'exactly', 
    'absolutely', 'you bet', 'right on', 'word', 'preach', 'true that',
    'i feel you', 'i hear you', 'i see you', 'wadap', 'xd', 'lol', 
    'lmao', 'rofl', 'haha', 'hehe', 'bruh', 'omg', 'wtf', 'tbh', 'imo', 'fyi',
    'idk', 'smh', 'tbh', 'ikr', 'bff', 'bae', 'srsly', 'frfr',
]

# KONDISI PERTAMA DIA INI for : Serious/Dangerous (Emergency)
SERIOUS_MEDICAL_KEYWORDS = [
    # Indonesian - Emergency conditions
    'darurat', 'emergency', 'urgent', 'kritis', 'meninggal', 'pingsan', 
    'kejang', 'kejang-kejang', 'sesak napas berat', 'napas berhenti',
    'nyeri dada hebat', 'nyeri dada berat', 'jantung berhenti',
    'darah banyak keluar', 'pendarahan berat', 'overdosis', 'keracunan',
    'tumor',
    
    # Indonesian - Severe symptoms
    'sesak napas', 'nyeri dada', 'pusing parah', 'pusing hebat',
    'demam tinggi', 'demam sangat tinggi', 'suhu sangat tinggi',
    'batuk darah', 'muntah darah', 'diare berdarah',
    'pingsan', 'tidak sadarkan diri', 'koma',
    
    # English - Emergency
    'emergency', 'urgent', 'critical', 'severe', 'fatal',
    'chest pain', 'shortness of breath', 'cannot breathe',
    'heavy bleeding', 'seizure', 'convulsion', 'fainting',
    'high fever', 'severe headache', 'unconscious', 'coma',
    'heart attack', 'stroke', 'cardiac arrest', 'overdose'
]

# KONDISI KE-2 DIA INI for : Light/Tips/Recommendations 
LIGHT_MEDICAL_KEYWORDS = [
    # Indonesian
    'rekomendasi', 'tips', 'saran', 'cara', 'rekomendasikan', 
    'merekomendasikan', 'rekom', 'sarankan', 'bagaimana cara',
    'kasih tahu', 'beri tahu', 'bantu kasih tips', 'bantu kasih saran',
    'bantu dengan tips', 'bantu dengan saran', 'dianjurkan', 'anjuran',
    'tips sehat', 'gaya hidup sehat', 'menu diet', 'olahraga',
    'vitamin apa', 'obat apa yang', 'makan apa yang',
    
    # English
    'recommendation', 'tip', 'advice', 'suggestion', 'recommend', 
    'suggest', 'advise', 'how to', 'recommend me', 'suggest me',
    'advise me', 'give me tips', 'give me advice', 'help with tips',
    'healthy lifestyle', 'diet plan', 'exercise routine', 'what to eat'
]

# KONDISI KE-3 DIA INI for : General Medical
MEDICAL_KEYWORDS = [
    # Indonesian - Symptoms & Conditions
    'gejala', 'sakit', 'penyakit', 'diagnosis', 'diagnosa', 'dokter', 'obat', 
    'hamil', 'kehamilan', 'demam', 'panas', 'batuk', 'pilek', 'flu', 'perut', 
    'sakit perut', 'kepala', 'pusing', 'jantung', 'ginjal', 'liver', 'hati',
    'infeksi', 'virus', 'bakteri', 'jamur', 'parasit',
    'alergi', 'gatal', 'bintik', 'ruam', 'kemerahan',
    'muntah', 'mual', 'mabuk', 'pening',
    'diare', 'konstipasi', 'sembelit', 'masuk angin',
    'darah', 'tekanan darah', 'kolesterol', 'diabetes', 'gula darah',
    'luka', 'bernanah', 'bengkak',
    'tulang', 'patah', 'retak', 'sendi', 'otot', 'saraf',
    'mata', 'telinga', 'hidung', 'tenggorokan', 'mulut', 'gigi',
    'kulit', 'rambut', 'kuku',
    'kanker', 'tumor', 'kista', 'benjolan',
    'asma', 'bronkitis', 'pneumonia', 'tb', 'tbc', 'paru',
    'maag', 'gerd', 'asam lambung', 'lambung',
    'stress', 'depresi', 'cemas', 'insomnia', 'gangguan tidur',
    
    # English - Symptoms & Conditions
    'symptom', 'symptoms', 'sick', 'sickness', 'disease', 'illness',
    'diagnosis', 'doctor', 'medicine', 'medication', 'drug', 'pill',
    'pregnant', 'pregnancy', 'fever', 'cough', 'cold', 'flu',
    'stomach', 'stomachache', 'head', 'headache', 'heart',
    'infection', 'virus', 'bacteria', 'fungus', 'parasite',
    'allergy', 'allergic', 'itchy', 'rash', 'hives',
    'vomit', 'nausea', 'dizziness', 'dizzy',
    'diarrhea', 'constipation', 'indigestion',
    'blood', 'blood pressure', 'cholesterol', 'diabetes', 'blood sugar',
    'wound', 'swelling', 'swollen', 'injury',
    'bone', 'muscle', 'joint', 'nerve', 'fracture',
    'eyes', 'ears', 'nose', 'throat', 'mouth', 'teeth', 'gums',
    'skin', 'hair', 'nails',
    'cancer', 'tumor', 'cyst', 'lump',
    'asthma', 'bronchitis', 'pneumonia', 'tb',
    'acid', 'reflux', 'gastritis', 'stomachache',
    'stress', 'depression', 'anxiety', 'insomnia', 'sleep disorder'
] + SERIOUS_MEDICAL_KEYWORDS

FAREWELL_KEYWORDS = [
    # Indonesian - Goodbye
    'terima kasih', 'makasih', 'thanks', 'thank you', 'thankyou',
    'selamat tinggal', 'sampai jumpa', 'salam', 'sampai nanti',
    'bye', 'bai', 'daah', 'dah', 'dada', 'dadah', 'dadaah', 'dah ya',
    'makasih banyak', 'terima kasih banyak', 'banyak terima kasih',
    'makasih ya', 'thanks ya', 'thank you very much',
    
    # English - Goodbye
    'goodbye', 'good bye', 'goodby', 'bye bye', 'byebye',
    'see you', 'see ya', 'catch you later', 'later',
    'take care', 'peace out', 'gtg', 'got to go', 'g2g',
    'thanks a lot', 'thank you so much', 'appreciate it',
    'cheers', 'much appreciated', 'thx', 'ty'
]




# ========================================================================    
#                    Bagian Prompt tleh ini kawan
# ========================================================================  

# Casual chat prompt (non-medical)
CASUAL_SYSTEM_PROMPT = """
Kamu temen dokter. Jawab natural ngobrol temen.

Rules:
- Bahasa Indo biasa, emoji cukup, bahasa inggris natural
- Ikuti flow user natural
- Tanya balik yang berhubungan dengan pertanyaan sebelumnya
- Ketika User menggunakan kata SLANG_INDO atau SLANG_ENG -> dengan menggunakan Words SLANG juga!

Chat history: {history}
User bertanya: {question}

Light disclaimer kalau medis light.
"""

# Light medical prompt (rekomendasi/tips)
MEDICAL_RAG_PROMPT = """
Kamu dokter AI yang santai tapi akurat dan profesional.

**INSTRUKSI:**
1. Jawab berdasarkan **KONTEKS MEDIS** yang diberikan
2. Jika konteks tidak cukup/tidak ada, gunakan pengetahuan umum medis
3. Format jawaban dengan jelas dan mudah dibaca

**PERINGATAN DARURAT:**
Jika pertanyaan mengandung kata-kata darurat (darurat, emergency, sesak napas, nyeri dada, kejang, dll), SELALU berikan:
- ⚠️ Tanda-tanda yang perlu segera ke IGD
- ⛔ Apa yang TIDAK boleh dilakukan
- 📞 Nomor darurat yang bisa dihubungi

**Konteks:**
{context}

**Pertanyaan:**
{question}

## 📋 RINGKASAN
[satu kalimat tentang inti masalah + kemungkinan diagnosis]

## 🔍 KEMUNGKINAN DIAGNOSIS
[Gunakan TABEL jika ada >1 kemungkinan]

| Kemungkinan Diagnosis | Alasan |
|----------------------|-------|
| [Diagnosis 1]        | [Alasan 1] |
| [Diagnosis 2]        | [Alasan 2] |
| [Diagnosis 3]        | [Alasan 3] |
| ...                  | ...   |
|----------------------|-------|

**Format Jawaban:**
1. **Kemungkinan diagnosis**: [penjelasan]
2. **Red flags (wajib ke dokter)**: [⚠️ list]
3. **Penjelasan singkat**: [paraphrase]
4. **Saran selanjutnya**: [✅ list]

---
⚠️ *Ini bukan pengganti konsultasi dokter. Selalu konsultasikan ke profesional kesehatan untuk diagnosis pasti.*
"""

LIGHT_MEDICAL_PROMPT = """
Kamu asisten kesehatan yang memberikan tips dan rekomendasi santai.

**INSTRUKSI:**
1. Berikan tips praktis yang mudah diikuti
2. Jawab dengan bahasa yang ramah dan santai
3. Tidak perlu terlalu teknis

**Pertanyaan:**
{question}

**Format Jawaban:**
**💡 Tips/Rekomendasi:**
- [Tips 1]
- [Tips 2]
- [Tips 3]

*Catatan: Ini hanya saran umum, bukan pengganti konsultasi dokter.*
"""


# Pure casual LLM fallback prompt
CASUAL_LLM_PROMPT = """
Kamu teman dokter yang chat santai dan friendly.

**ATURAN:**
- Bahasa natural, campur Indo-English kalau biasa
- Pakai emoji secukupnya (tapi jangan berlebihan)
- Tanya balik kalau perlu klarifikasi
- Kalau topik medis → kasih disclaimer

**Chat History:**
{history}

**User:**
{question}

**Format:**
[Jawab natural, friendly, pakai emoji jika cocok]
"""

FAREWELL_PROMPT = """
Kamu asisten kesehatan yang friendly. User sedang mengucap salam perpisahan.

**ATURAN:**
1. Jawab dengan hangat dan friendly
2. Jangan terlalu panjang - singkat dan sweet
3. Pakai emoji yang sesuai
4. Jika ada topik kesehatan yang belum dibahas → boleh kasih reminder singkat

**Contoh Response:**
- "Sama-sama! 😊 Semoga sehat selalu ya! Kalau ada yang mau ditanya lagi, jangan ragu. Bye!"
- "Oke sama-sama! Jaga kesehatan sempre! Kalau butuh bantuan lagi, siap sedia di sini! 👋"
- "Makasih juga! Stay healthy ya! See you next time! "
- "Makaseh banya ehh, Semoga ngna sehat" terus mar kalo ngna mo ba tanya ulang, langsung jo nd usah malo malo 😊"

---

⚠️ *Disclaimer: Ini bukan pengganti konsultasi dokter. Selalu konsultasikan ke profesional kesehatan.*
"""


# ========================================================================   
#                   Bagian Pangge Fungsi Prompt
# ========================================================================   

# Function untuk detect medical query
def is_light_medical(text: str) -> bool:
    # Detect rekomendasi/tips
    text_lower = text.lower()
    return any(keyword in text_lower for keyword in LIGHT_MEDICAL_KEYWORDS)

def is_serious_medical(text: str) -> bool:
    # Detect darurat/serious
    text_lower = text.lower()
    return any(keyword in text_lower for keyword in SERIOUS_MEDICAL_KEYWORDS)

def is_medical_query(text: str) -> bool:
    # Auto-detect medis umum
    text_lower = text.lower()
    return any(keyword in text_lower for keyword in MEDICAL_KEYWORDS) and not is_light_medical(text) and not is_serious_medical(text)

# Language detector simple
def detect_language(text: str) -> str:
    # Deteksi bahasa utama dalam teks
    text_lower = text.lower()
    indo_score = sum(1 for word in SLANG_INDO if word in text_lower)
    eng_score = sum(1 for word in SLANG_ENG if word in text_lower)
    
    if eng_score > indo_score:
        return "English"
    return "Indonesian"  # Default ke Indonesian

# Detect Farewell 
def is_farewell(text: str) -> bool:
    """Deteksi salam perpisahan atau terima kasih"""
    text_lower = text.lower()
    return any(keyword in text_lower for keyword in FAREWELL_KEYWORDS)