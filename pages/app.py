import streamlit as st
from pathlib import Path
from langchain_ollama import ChatOllama
from pages.rag_engine import HybridMedicalRAG

# Disclaimer sadiki jadi kwa ini bagian senitive jangan talalu banya kore disni
# karna so saki nih kapala da beking beking so 2 minggu nda kelar kelar anjerrrr
# Semoga saling memahami noh katu.


#------------------------------------------------------------#
# Bagian UI atau tampilan Streamlit.
#------------------------------------------------------------#
# ==================== CONFIG TAB WEB ====================
st.set_page_config(
    page_title="Medical Health - Assistant",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==================== HEADER ====================
st.markdown("""
<div class="medical-header">
    <h1>Medical Health Assistant</h1>
    <p>Your personal AI-powered Health Assistant!</p>
</div>
""", unsafe_allow_html=True)

# ==================== CUSTOM NAVBAR ====================
st.markdown("""
<style>
    /* Hide default Streamlit header */
    [data-testid="stHeader"] {
        display: none !important;
    }
    
    /* Hide Streamlit menu & deploy button */
    #MainMenu { display: none !important; }
    .stAppDeployButton { display: none !important; }
    [data-testid="stDecoration"] { display: none !important; }
    [data-testid="stToolbar"] { display: none !important; }
</style>
""", unsafe_allow_html=True)

# ==================== CUSTOM NAVBAR HTML ====================
st.markdown("""
<div class="navbar">
    <div class="nav-left">
        <div class="logo-text">❤️‍🩹MHAR</div>
        <div class="logo-sub">Medical Health Assistant RAG</div>
    </div>
    <div class="nav-right">
        <a href="/des" target="_self" class="cta" style="margin-top: 2.5px;">Home</a>
        <div class="status-indicator">
            <div class="pulse-dot"></div>
            <span>Online</span>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ==================== CUSTOM CSS MEDICAL THEME ====================
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
    
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }
    
    /* ========== CSS VARIABLES ========== */
    :root {
        --primary-100: #a78bfa;
        --primary-300: #c4b5fd;
        --primary-500: #7c3aed;
        --primary-700: #6d28d9;
        --primary-900: #4c1d95;
        --accent-pink: #ec4899;
        --accent-teal: #14b8a6;
        --bg-dark: #0a0614;
        --bg-card: rgba(124, 58, 237, 0.08);
        --text-primary: #e2e8f0;
        --text-muted: rgba(167, 139, 250, 0.5);
        --border-subtle: rgba(124, 58, 237, 0.2);
        --shadow-glow: 0 0 20px rgba(124, 58, 237, 0.3);
    }
            
    /* ========== BACKGROUND - FIXED ========== */
    .stApp {
        background-color: #0a0614 !important;
        background-image: 
            radial-gradient(ellipse at 20% 20%, rgba(124, 58, 237, 0.15) 0%, transparent 50%),
            radial-gradient(ellipse at 80% 80%, rgba(236, 72, 153, 0.1) 0%, transparent 50%);
    }
            
    /* ========== CUSTOM NAVBAR ========== */
    .navbar {
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        height: 64px;
        background: linear-gradient(180deg, rgba(15, 10, 30, 0.98) 0%, rgba(15, 10, 30, 0.92) 100%) !important;
        backdrop-filter: blur(20px) !important;
        -webkit-backdrop-filter: blur(20px) !important;
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 0 24px;
        z-index: 9999;
        border-bottom: 1px solid var(--border-subtle);
        box-shadow: 0 4px 30px rgba(0, 0, 0, 0.3), 0 0 60px rgba(124, 58, 237, 0.05);
        animation: slideDown 0.5s ease-out;
    }
    
    @keyframes slideDown {
        from { opacity: 0; transform: translateY(-100%); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    .nav-left {
        display: flex;
        align-items: center;
        gap: 12px;
    }
    
    .logo-text {
        font-size: 24px;
        font-weight: 800;
        color: #ffffff !important;
        letter-spacing: 1px;
        text-shadow: 0 2px 10px rgba(255, 255, 255, 0.3);
    }

    .logo-sub {
        font-size: 11px;
        color: rgba(255, 255, 255, 0.8) !important;
        font-weight: 400;
        letter-spacing: 2px;
        text-transform: uppercase;
        padding-left: 12px;
        border-left: 1px solid rgba(255, 255, 255, 0.2);
    }
    
    .nav-right {
        display: flex;
        align-items: center;
        gap: 16px;
    }
    
    .cta {
        background: #7c3aed !important;
        color: white !important;
        border: none !important;
        padding: 8px 18px !important;
        border-radius: 10px !important;
        font-weight: 600 !important;
        cursor: pointer !important;
        transition: 0.3s !important;
        text-decoration: none !important;
        display: inline-block !important;
        opacity: 1 !important;
    }

    .cta:hover {
        background: #6d28d9 !important;
        color: white !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 10px 20px rgba(124, 58, 237, 0.3) !important;
    }
    
    .status-indicator {
        display: flex;
        align-items: center;
        gap: 8px;
        padding: 8px 14px;
        background: rgba(16, 185, 129, 0.1);
        border: 1px solid rgba(16, 185, 129, 0.2);
        border-radius: 20px;
        font-size: 12px;
        color: #10b981;
        font-weight: 500;
    }
    
    .pulse-dot {
        width: 8px;
        height: 8px;
        background: #10b981;
        border-radius: 50%;
        animation: pulse-online 2s infinite;
        box-shadow: 0 0 10px rgba(16, 185, 129, 0.5);
    }
    
    @keyframes pulse-online {
        0% { box-shadow: 0 0 0 0 rgba(16, 185, 129, 0.7); }
        70% { box-shadow: 0 0 0 8px rgba(16, 185, 129, 0); }
        100% { box-shadow: 0 0 0 0 rgba(16, 185, 129, 0); }
    }
    
    /* ========== EKG ANIMATION ========== */
    .ekg-container {
        display: flex;
        align-items: flex-end;
        gap: 3px;
        height: 30px;
        padding: 10px;
        justify-content: center;
    }

    .ekg-bar {
        width: 6px;
        background: linear-gradient(to top, var(--primary-500), var(--primary-100)) !important;
        border-radius: 3px 3px 0 0;
        animation: ekg-pulse 1.2s ease-in-out infinite;
        will-change: height;
    }

    .ekg-bar:nth-child(1) { animation-delay: 0.0s; }
    .ekg-bar:nth-child(2) { animation-delay: 0.1s; height: 10px !important; }
    .ekg-bar:nth-child(3) { animation-delay: 0.15s; height: 12px !important; }
    .ekg-bar:nth-child(4) { animation-delay: 0.2s; height: 10px !important; }
    .ekg-bar:nth-child(5) { animation-delay: 0.25s; height: 12px !important; }
    .ekg-bar:nth-child(6) { animation-delay: 0.3s; height: 10px !important; }
    .ekg-bar:nth-child(7) { animation-delay: 0.35s; height: 14px !important; }
    .ekg-bar:nth-child(8) { 
        animation-delay: 0.4s; 
        height: 26px !important; 
        background: var(--accent-pink) !important; 
        width: 8px !important; 
    }
    .ekg-bar:nth-child(9) { animation-delay: 0.5s; height: 12px !important; }
    .ekg-bar:nth-child(10) { animation-delay: 0.55s; height: 10px !important; }
    .ekg-bar:nth-child(11) { animation-delay: 0.6s; height: 12px !important; }
    .ekg-bar:nth-child(12) { animation-delay: 0.65s; height: 8px !important; }

    @keyframes ekg-pulse {
        0%, 100% { transform: scaleY(1); opacity: 0.7; }
        50% { transform: scaleY(1.5); opacity: 1; }
    }

    /* ========== CHAT MESSAGES ========== */
    .chat-user {
        background: linear-gradient(135deg, var(--primary-500) 0%, var(--primary-700) 100%) !important;
        color: white !important;
        border-radius: 18px 18px 4px 18px !important;
        padding: 12px 16px !important;
        max-width: 75%;
        font-size: 15px;
        line-height: 1.5;
    }
    
    .chat-assistant {
        background: var(--bg-card) !important;
        border: 1px solid var(--border-subtle) !important;
        color: var(--text-primary) !important;
        border-radius: 18px 18px 18px 4px !important;
        padding: 12px 16px !important;
        backdrop-filter: blur(12px);
        max-width: 75%;
        font-size: 15px;
        line-height: 1.6;
    }
            
    /* ========== CHAT INPUT (Custom Prompt Used) ========== */
    [data-testid="stBottomBlockContainer"] {
        display: none !important;
    }
    
    /* ========== CUSTOM PROMPT BAR ========== */
    div[data-testid="stForm"] {
        position: fixed !important;
        bottom: 24px !important;
        left: 50% !important;
        transform: translateX(-50%) !important;
        width: calc(100% - 48px) !important;
        max-width: 720px !important;
        z-index: 9998 !important;
        padding: 0 !important;
        background: transparent !important;
        border: none !important;
    }
    
    div[data-testid="stForm"] > div {
        background: linear-gradient(145deg, #1a1a2e 0%, #0f0f1a 100%) !important;
        border: 1px solid rgba(255, 255, 255, 0.08) !important;
        border-radius: 28px !important;
        padding: 14px 14px 14px 20px !important;
        display: flex !important;
        align-items: center !important;
        gap: 12px !important;
        box-shadow: 
            0 8px 32px rgba(0, 0, 0, 0.6),
            0 0 0 1px rgba(255, 255, 255, 0.05),
            inset 0 1px 0 rgba(255, 255, 255, 0.05) !important;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
    }
    
    div[data-testid="stForm"] > div:focus-within {
        border-color: rgba(124, 58, 237, 0.4) !important;
        box-shadow: 
            0 12px 48px rgba(0, 0, 0, 0.8),
            0 0 0 1px rgba(124, 58, 237, 0.3),
            0 0 40px rgba(124, 58, 237, 0.15) !important;
    }
    
    div[data-testid="stForm"] input {
        background: transparent !important;
        border: none !important;
        outline: none !important;
        color: #ffffff !important;
        font-size: 14px !important;
        font-family: 'Inter', -apple-system, sans-serif !important;
        caret-color: #a78bfa !important;
        padding: 6px 0 !important;
        flex: 1 !important;
    }
    
    div[data-testid="stForm"] input::placeholder {
        color: rgba(255, 255, 255, 0.35) !important;
    }
    
    div[data-testid="stForm"] button {
        background: linear-gradient(135deg, #7c3aed 0%, #6d28d9 100%) !important;
        border: none !important;
        border-radius: 50% !important;
        width: 42px !important;
        height: 42px !important;
        min-width: 42px !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        cursor: pointer !important;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
        flex-shrink: 0 !important;
    }
            
    div[data-testid="stForm"] button::before {
        content: '' !important;
        position: absolute !important;
        width: 18px !important;
        height: 18px !important;
        background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' fill='none' viewBox='0 0 24 24' stroke='white' stroke-width='2'%3E%3Cpath stroke-linecap='round' stroke-linejoin='round' d='M6 12L3.269 3.126A59.768 59.768 0 0121.485 12 59.77 59.77 0 013.27 20.876L5.999 12zm0 0h7.5'/%3E%3C/svg%3E") !important;
        background-repeat: no-repeat !important;
        background-position: center !important;
        background-size: contain !important;
    }
    
    div[data-testid="stForm"] button:hover {
        background: linear-gradient(135deg, #8b5cf6 0%, #7c3aed 100%) !important;
        transform: scale(1.08) !important;
        box-shadow: 0 4px 20px rgba(124, 58, 237, 0.5) !important;
    }
    
    div[data-testid="stForm"] button p {
        display: none !important;
    }
    
    /* ========== RESPONSIVE ========== */
    @media (max-width: 768px) {
        div[data-testid="stForm"] {
            bottom: 16px !important;
            width: calc(100% - 32px) !important;
        }
        
        div[data-testid="stForm"] > div {
            padding: 10px 10px 10px 16px !important;
            border-radius: 22px !important;
        }
        
        div[data-testid="stForm"] button {
            width: 38px !important;
            height: 38px !important;
            min-width: 38px !important;
        }
    }
    
    /* ========== SIDEBAR ========== */
    [data-testid="stSidebar"] {
        background: rgba(5, 3, 13, 0.95) !important;
        backdrop-filter: blur(24px);
        border-right: 1px solid var(--border-subtle) !important;
    }
    
    [data-testid="stSidebarHeader"] {
        color: var(--text-primary) !important;
    }
    
    .stats-card {
        background: var(--bg-card) !important;
        border: 1px solid var(--border-subtle) !important;
        border-radius: 12px !important;
        padding: 16px !important;
        text-align: center;
    }
    
    .file-info {
        background: rgba(124, 58, 237, 0.06);
        border: 1px solid var(--border-subtle);
        border-radius: 12px;
        padding: 12px;
        margin-top: 10px;
    }
    
    .file-info-header {
        color: var(--primary-100);
        font-weight: 600;
        margin-bottom: 8px;
        font-size: 14px;
    }
    
    .file-info-row {
        display: flex;
        justify-content: space-between;
        font-size: 12px;
        color: var(--text-muted);
        padding: 4px 0;
        border-bottom: 1px solid rgba(124, 58, 237, 0.1);
    }
    
    .file-info-row:last-child {
        border-bottom: none;
    }
    
    .uploaded-file {
        background: rgba(124, 58, 237, 0.06);
        border: 1px solid var(--border-subtle);
        border-radius: 8px;
        padding: 10px;
        margin-bottom: 8px;
        font-size: 13px;
    }
    
    .uploaded-file small {
        color: var(--text-muted);
    }
            
        /* ========== ALERT BOXES ========== */
    .stInfo, .stWarning, .stError, .stSuccess {
        border-radius: 12px !important;
        padding: 12px 16px !important;
    }
    
    .stInfo {
        background: rgba(124, 58, 237, 0.1) !important;
        border: 1px solid rgba(124, 58, 237, 0.3) !important;
        color: var(--text-primary) !important;
    }
    
    .stWarning {
        background: rgba(245, 158, 11, 0.1) !important;
        border: 1px solid rgba(245, 158, 11, 0.3) !important;
        color: #fbbf24 !important;
    }
    
    .stError {
        background: rgba(239, 68, 68, 0.1) !important;
        border: 1px solid rgba(239, 68, 68, 0.3) !important;
        color: #f87171 !important;
    }
    
    .stSuccess {
        background: rgba(16, 185, 129, 0.1) !important;
        border: 1px solid rgba(16, 185, 129, 0.3) !important;
        color: #34d399 !important;
    }

        /* ========== HEADER ========== */
    .medical-header {
        text-align: center;
        padding: 20px 0;
        margin-top: 80px;
    }
    
    .medical-header h1 {
        color: #ffffff !important;
        font-size: 2.5rem;
        font-weight: 700;
        margin-bottom: 8px;
        text-shadow: 0 2px 10px rgba(0, 0, 0, 0.3);
    }
    
    .medical-header p {
        color: rgba(255, 255, 255, 0.7) !important;
        font-size: 1rem;
        font-weight: 400;
    }
    
    /* ========== PROGRESS UI ========== */
    .progress-container {
        display: flex;
        flex-direction: column;
        gap: 12px;
        padding: 16px;
        background: var(--bg-card);
        border-radius: 12px;
        border: 1px solid var(--border-subtle);
    }
    
    .progress-step {
        display: flex;
        align-items: center;
        gap: 12px;
        font-size: 14px;
        color: var(--text-muted);
        transition: all 0.3s ease;
    }
    
    .progress-step.completed {
        color: var(--primary-500);
    }
    
    .progress-step.active {
        color: var(--primary-100);
        font-weight: 600;
    }
    
    .step-icon {
        font-size: 18px;
        width: 24px;
        text-align: center;
    }
    
    .step-icon.completed {
        color: var(--primary-500);
    }
    
    .step-icon.active {
        color: var(--primary-100);
        animation: spin 1s linear infinite;
    }
    
    .step-icon.pending {
        color: var(--text-muted);
    }
    
    @keyframes spin {
        from { transform: rotate(0deg); }
        to { transform: rotate(360deg); }
    }
    
    /* ========== SCROLLBAR ========== */
    ::-webkit-scrollbar {
        width: 6px;
        height: 6px;
    }
    
    ::-webkit-scrollbar-track {
        background: rgba(5, 3, 13, 0.5);
        border-radius: 10px;
    }
    
    ::-webkit-scrollbar-thumb {
        background: rgba(124, 58, 237, 0.3);
        border-radius: 10px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: rgba(124, 58, 237, 0.5);
    }
    
    /* ========== FOOTER ========== */
    [data-testid="stCaption"] {
        color: var(--text-muted) !important;
        font-size: 12px !important;
        text-align: center !important;
        font-weight: 400 !important;
        padding: 8px 0;
    }
    
    /* ========== BUTTONS ========== */
    [data-testid="stBaseButton-secondary"] {
        background: rgba(124, 58, 237, 0.1) !important;
        border: 1px solid var(--border-subtle) !important;
        color: var(--primary-100) !important;
        border-radius: 12px !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 4px 12px rgba(124, 58, 237, 0.15) !important;
    }
    
    [data-testid="stBaseButton-secondary"]:hover {
        background: rgba(124, 58, 237, 0.2) !important;
        border-color: rgba(124, 58, 237, 0.5) !important;
        color: var(--primary-300) !important;
        box-shadow: 0 6px 20px rgba(124, 58, 237, 0.25) !important;
        transform: translateY(-1px) !important;
    }
    
    /* ========== METRIC CARDS ========== */
    [data-testid="stMetric"] {
        background: var(--bg-card) !important;
        border: 1px solid var(--border-subtle) !important;
        border-radius: 12px !important;
        padding: 16px !important;
    }
    
    [data-testid="stMetricLabel"] {
        color: var(--text-muted) !important;
    }
    
    [data-testid="stMetricValue"] {
        color: var(--primary-100) !important;
    }
    
    /* ========== FILE UPLOADER ========== */
    [data-testid="stFileUploader"] {
        background: rgba(124, 58, 237, 0.05) !important;
        border: 2px dashed var(--border-subtle) !important;
        border-radius: 12px !important;
        padding: 20px !important;
    }
    
    /* ========== PROGRESS BAR ========== */
    .stProgress > div > div > div > div {
        background: linear-gradient(90deg, var(--primary-500), var(--primary-100), var(--accent-pink)) !important;
        border-radius: 10px !important;
    }
    
    /* ========== DIVIDER ========== */
    hr {
        border: none !important;
        height: 2px !important;
        background: linear-gradient(90deg, transparent 0%, var(--primary-500) 50%, transparent 100%) !important;
        box-shadow: 0 0 10px rgba(124, 58, 237, 0.5) !important;
        margin: 20px 0 !important;
    }        

    /* ========== RESPONSIVE - ENHANCED ========== */
    @media (max-width: 768px) {
        .navbar {
            padding: 0 12px;
            height: 56px;
        }
        
        .logo-text {
            font-size: 24px;
            font-weight: 800;
            color: #ffffff !important;
            letter-spacing: 1px;
            text-shadow: 0 2px 10px rgba(255, 255, 255, 0.3);
        }
        
        .logo-sub {
            font-size: 11px;
            color: rgba(255, 255, 255, 0.8) !important;
            font-weight: 400;
            letter-spacing: 2px;
            text-transform: uppercase;
            padding-left: 12px;
            border-left: 1px solid rgba(255, 255, 255, 0.2);
        }
        
        .cta {
            padding: 8px 14px;
            font-size: 12px;
        }
        
        .status-indicator {
            padding: 6px 10px;
            font-size: 11px;
        }
        
        .chat-user, .chat-assistant {
            max-width: 88%;
        }
        
        .ekg-bar {
            width: 4px;
        }
    }

    @media (max-width: 480px) {
        .navbar {
            height: 50px;
        }
        
        .logo-text {
            font-size: 24px;
            font-weight: 800;
            color: #ffffff !important;
            letter-spacing: 1px;
            text-shadow: 0 2px 10px rgba(255, 255, 255, 0.3);
        }
        
        .cta {
            padding: 6px 12px;
            font-size: 11px;
        }
        
        .ekg-container {
            height: 24px;
        }
    }
    
    @media (min-width: 1024px) {
        .logo-sub {
            font-size: 10px;
            padding-left: 10px;
        }
    }
            
    div[data-testid="stForm"] small {
        display: none !important;
    }
            
    [data-testid="stSidebarNav"] {
        display: none !important;
    }
            
</style>
""", unsafe_allow_html=True)

# ==================== EKG ANIMATION ====================
st.markdown("""
<div class="ekg-container">
    <div class="ekg-bar"></div>
    <div class="ekg-bar"></div>
    <div class="ekg-bar"></div>
    <div class="ekg-bar"></div>
    <div class="ekg-bar"></div>
    <div class="ekg-bar"></div>
    <div class="ekg-bar"></div>
    <div class="ekg-bar"></div>
    <div class="ekg-bar"></div>
    <div class="ekg-bar"></div>
    <div class="ekg-bar"></div>
    <div class="ekg-bar"></div>
</div>
""", unsafe_allow_html=True)



#------------------------------------------------------------#
# Bagian Codenya atau Logic dari RAG dan LLM. (Back-End)
#------------------------------------------------------------#

# ==================== HELPER FUNCTIONS ====================
def show_progress_ui(steps, current_step, progress_value):
    icons = {"pending": "○", "active": "◐", "completed": "✓"}
    html = '<div class="progress-container">'
    
    for i, step in enumerate(steps):
        if i < current_step:
            status, icon = "completed", icons["completed"]
        elif i == current_step:
            status, icon = "active", icons["active"]
        else:
            status, icon = "pending", icons["pending"]
        html += f'<div class="progress-step {status}"><div class="step-icon {status}">{icon}</div><span>{step}</span></div>'
    
    html += '</div>'
    html += f'''
    <div style="margin-top: 12px;">
        <div style="display: flex; justify-content: space-between; font-size: 11px; color: #94a3b8; margin-bottom: 6px;">
            <span>Progress</span><span>{int(progress_value * 100)}%</span>
        </div>
        <div style="background: rgba(255,255,255,0.1); border-radius: 10px; height: 8px; overflow: hidden;">
            <div style="background: linear-gradient(90deg, #14b8a6, #5eead4); height: 100%; width: {progress_value * 100}%; border-radius: 10px; transition: width 0.3s ease;"></div>
        </div>
    </div>
    '''
    return html

def show_file_info(filename, file_size, file_type):
    if file_size < 1024:
        size_str = f"{file_size} B"
    elif file_size < 1024 * 1024:
        size_str = f"{file_size / 1024:.1f} KB"
    else:
        size_str = f"{file_size / (1024 * 1024):.1f} MB"
    
    return f'''
    <div class="file-info">
        <div class="file-info-header">📄 File Information</div>
        <div class="file-info-row"><span>Nama File</span><span>{filename}</span></div>
        <div class="file-info-row"><span>Ukuran</span><span>{size_str}</span></div>
        <div class="file-info-row"><span>Tipe</span><span>{file_type.upper()}</span></div>
        <div class="file-info-row"><span>Status</span><span>✓ Siap Diproses</span></div>
    </div>
    '''

def handle_query(prompt):
    result = st.session_state.rag_engine.query(prompt)
    return result

#=========== Session State Initialization ========= 
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "🏥 Halo! Selamat Datang di Medical Health Assistant.\n\n"
        "Saya asisten kesehatan digital Anda. Silakan tanyakan tentang:\n\n"
        "• 📋 Informasi kesehatan umum\n"
        "• 💊 Obat-obatan & Farmasi\n•"
        " 🩺 Gejala penyakit\n"
        "• 🥗 Nutrisi & Gaya hidup sehat\n"
        "• 📄 Analisis dokumen medis (PDF)\n\n"
        "• 🟢 English and Indonesia\n\n"
        "*Catatan: Saya hanya Assistant, bukan Dokter Profesional.*"}
    ]
    
if 'uploaded_files_info' not in st.session_state:
    st.session_state.uploaded_files_info = []
    
if 'current_file_name' not in st.session_state:
    st.session_state.current_file_name = None
    
if 'upload_progress' not in st.session_state:
    st.session_state.upload_progress = 0
    
if "rag_engine" not in st.session_state:
    st.session_state.rag_engine = HybridMedicalRAG()


# ==================== SIDEBAR ====================
with st.sidebar:
    st.markdown("## 🏥 Medical Health RAG")
    st.markdown("---")
    
    # File Upload Section
    st.markdown("### 📂 Upload Dokumen")
    
    uploaded_file = st.file_uploader(
        "Pilih file PDF atau TXT",
        type=['pdf', 'txt'],
        help="Upload dokumen untuk ditambahkan ke knowledge base"
    )
    
    if uploaded_file:
        if st.session_state.current_file_name != uploaded_file.name:
            st.session_state.current_file_name = uploaded_file.name
            
            save_dir = Path("uploaded_docs")
            save_dir.mkdir(exist_ok=True)
            file_path = save_dir / uploaded_file.name
            
            with open(file_path, "wb") as f:
                f.write(uploaded_file.getbuffer())
            
            progress_bar = st.progress(0, text="Memproses...")
            
            # ✅ FIX: process_document() sekarang ada
            success = st.session_state.rag_engine.process_document(str(file_path))
            progress_bar.empty()
            
            if success:
                st.session_state.uploaded_files_info.append({
                    "name": uploaded_file.name,
                    "size": round(uploaded_file.size / 1024, 1),
                    "time": "Baru saja"
                })
            else:
                st.error("❌ Gagal memproses file.")
    
    st.markdown("---")
    
    # Stats Section
    st.markdown("### 📊 Status Sistem")
    
    stats = st.session_state.rag_engine.get_stats()
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"""
        <div class="stats-card">
            <div style="font-size: 2rem;">{'✅' if stats['has_vectorstore'] else '⚠️'}</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="stats-card">
            <div style="font-size: 2rem;">{stats['chat_history_size']}</div>
            <div style="font-size: 0.8rem;">Chat History</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown(f"""
    **Model:** `{stats['model']}`  
    **Sample Data:** {stats['sample_knowledge_size']} items
    """)
    
    # Uploaded Files List
    if st.session_state.uploaded_files_info:
        st.markdown("### 📁 File Terupload")
        for file_info in st.session_state.uploaded_files_info:
            st.markdown(f"""
            <div class="uploaded-file">
                📄 {file_info['name']}<br>
                <small>{file_info['size']} KB • {file_info['time']}</small>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Clear Chat History
    if st.button("🗑️ Clear Chat History", use_container_width=True):
        st.session_state.rag_engine.clear_chat_history()
        st.session_state.messages = []
        st.rerun()


# ==================== OLLAMA CHECK ====================
try:
    import ollama
    st.sidebar.success("✅ Ollama Connected !")
except:
    st.sidebar.error("❌ Run: `ollama serve`")
model_name = "llama3.2:3b"

def get_llm(temp=0.2):
    return ChatOllama(model=model_name, temperature=temp)

# ==================== Main Content====================
chat_container = st.container()

with chat_container:
    # Display Chat History
    if st.session_state.messages:
        for msg in st.session_state.messages:
            if msg["role"] == "user":
                st.markdown(f'''
                <div style="display:flex; justify-content:flex-end; align-items:flex-end; margin:10px 0;">
                    <div class="chat-user">
                        {msg["content"]}
                    </div>
                    <img src="https://i.pravatar.cc/40?img=7" alt="User" style="
                        width: 40px; height: 40px; border-radius: 50%; margin-left: 10px;">
                </div>
                ''', unsafe_allow_html=True)

            else:
                st.markdown(f'''
                <div style="display:flex; justify-content:flex-start; align-items:flex-start; margin:10px 0;">
                    <img src="https://cdn-icons-png.flaticon.com/512/4712/4712085.png" alt="AI" style="
                        width: 40px; height: 40px; border-radius: 50%; margin-right: 10px;">
                    <div class="chat-assistant">
                        {msg["content"]}
                    </div>
                </div>
                ''', unsafe_allow_html=True)
    else:
        # Welcome Message
        st.markdown('''
        <div style="text-align: center; padding: 50px 20px; color: rgba(255,255,255,0.8);">
            <div style="font-size: 4rem; margin-bottom: 20px;">🤖</div>
            <h3>Selamat Datang Di Medical Health - Assistant</h3>
            <p>Tanyakan apa saja tentang kesehatan. Saya siap membantu!</p>
        </div>
        ''', unsafe_allow_html=True)

 
# ==================== CHAT FORM ====================
if "pending_input" not in st.session_state:
    st.session_state.pending_input = ""

with st.form(key="medical_chat_form_final_v2", clear_on_submit=True):
    col1, col2 = st.columns([1, 0.08])
    
    with col1:
        user_input = st.text_input(
            label="Chat",
            key="medical_chat_input_final_v2",
            label_visibility="collapsed",
            placeholder="Bertanya apa saja tentang kesehatan..."
        )
    
    with col2:
        submitted = st.form_submit_button("▶", use_container_width=True)

# ==================== HANDLE THE INPUT ====================
if submitted and user_input and user_input.strip():
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })
    
    with st.spinner(" Sedang Berpikir..."):
        result = st.session_state.rag_engine.query(user_input)
    
    st.session_state.messages.append({
        "role": "assistant",
        "content": result["answer"]
    })
    
    st.rerun()
    
    # Clear input after processing (jika masih ada)
    st.session_state["medical_chat_input_unique_2024"] = ""

# ==================== FOOTER ====================
st.markdown("---")

st.caption("Create By : Group 7 - Expert Systems - Universitas Klabat")
st.caption("Medical RAG Version : 5.3 - Updated 01 Mei 2026")
st.caption("© 2026 Medical Health Assistant. All rights reserved.")