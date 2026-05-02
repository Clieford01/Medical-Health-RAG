import streamlit as st
import base64
import os

# --- KONFIGURASI HALAMAN ---
st.set_page_config(page_title="MHAR - Medical Health Assistant", layout="wide")


# --- FUNGSI UNTUK MEMBACA GAMBAR LOKAL ---
def get_base64_img(img_path):
    if os.path.exists(img_path):
        with open(img_path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    return ""


img_tim1 = get_base64_img("images/ipot.png")
img_tim2 = get_base64_img("images/riel.png")
img_tim3 = get_base64_img("images/monic.png")
img_tim4 = get_base64_img("images/eji.png")
img_tim5 = get_base64_img("images/osep.png")

# --- LOAD CSS EXTERNAL ---
try:
    with open("styles_1/style_1.css", encoding="utf-8") as f:
        css_content = f.read()
except FileNotFoundError:
    css_content = ""

# --- 1. CSS DIPISAH (PENTING: Agar tidak bentrok f-string) ---
st.markdown(f"<style>{css_content}</style>", unsafe_allow_html=True)

# --- 2. CSS TAMBAHAN UNTUK FIX GAMBAR (Hard Override) ---
st.markdown(
    """
<style>
.photo-box {
    width: 100% !important;
    aspect-ratio: 1 / 1 !important;
    overflow: hidden !important;
    display: block !important;
}
.team-img {
    width: 100% !important;
    height: 100% !important;
    object-fit: cover !important; /* INI KUNCINYA: Zoom & Fill */
    object-position: center !important;
}
</style>
""",
    unsafe_allow_html=True,
)

# --- 3. HTML STRUCTURE (Tanpa CSS di dalamnya) ---
st.markdown(
    f"""
<div class="main-wrapper">
    <!-- NAVBAR -->
    <div class="navbar-sensor"></div>
    <div class="navbar">
        <div class="nav-left">
            <div class="logo-text">❤️‍🩹MHAR</div>
        </div>
        <div class="nav-right">
            <!-- Menghapus About, Home lama, dan Contact -->
            <button class="cta">Home</button>
        </div>
    </div>
    <div class="hero">
        <div class="hero-content">
            <div class="icon"></div>
            <div class="hero-title">Medical Health<br>Assistant</div>
            <p style="margin-top: 20px;">RASA SAKI? COBA TANYA DISINI ↓</p>
            <a href="app" target="_self" class="cta" style="margin-top: 30px;">SINI</a>
        </div>
    </div>
<section class="about-section">
    <div class="about-title">About Us</div>
    <div class="team-grid">
        <!-- ANGGOTA 1 -->
        <div class="team-card">
            <div class="photo-box">
                <img src="data:image/png;base64,{img_tim1}" class="team-img">
            </div>
            <div class="team-info">
                <h4>Pangemanan, Clieford \n(105022410084)</h4>
                <p>• Back-End RAG Processing</p>
                <p>• Helping UI/UX</p>
                <p>• Create Logic</p>
                <p>• Searching for journals</p>
            </div>
        </div>
        <!-- ANGGOTA 2 -->
        <div class="team-card">
            <div class="photo-box">
                <img src="data:image/png;base64,{img_tim2}" class="team-img">
            </div>
            <div class="team-info">
                <h4>Mandang, Ariel Quinn \n(105022410126)</h4>
                <p>• Output-Feedback-Continuous Learning</p>
                <p>• Design Ideas</p>
                <p>• Design UI/UX</p>
                <p>• Searching for journals</p>
            </div>
        </div>
        <!-- ANGGOTA 3 -->
        <div class="team-card">
            <div class="photo-box">
                <img src="data:image/png;base64,{img_tim3}" class="team-img">
            </div>
            <div class="team-info">
                <h4>Mudeng, Monica Maria \n(105022410085)</h4>
                <p>• input and safety gate</p>
                <p>• Searching for journals</p>
                <p>• AI Photo Editor</p>
            </div>
        </div>
        <!-- ANGGOTA 4 -->
        <div class="team-card">
            <div class="photo-box">
                <img src="data:image/png;base64,{img_tim4}" class="team-img">
            </div>
            <div class="team-info">
                <h4>Hosang, Euginio Juliando\n(105022410055)</h4>
                <p>• Medical Knowledge Base</p>
                <p>• Searching for journals</p>
            </div>
        </div>
        <!-- ANGGOTA 5 -->
        <div class="team-card">
            <div class="photo-box">
                <img src="data:image/png;base64,{img_tim5}" class="team-img">
            </div>
            <div class="team-info">
                <h4>Polii, Joseph Benyamin \n(105022410091)</h4>
                <p>• Confidence Check & Generation</p>
                <p>• Searching for journals</p>
            </div>
        </div>
    </div>
</section>
    <div class="footer">
<div class="footer-left">
    <div class="footer-title">Contact</div>
    <!-- Link WA - Pastikan format angka murni 62... -->
    <a href="https://wa.me/+6282191946423" target="_blank" class="footer-link-wa">+62 821-9194-6423 - Clieford</a>
    <a href="https://wa.me/+6287776597977" target="_blank" class="footer-link-wa">+62 877-7659-7977 - Ariel</a>
    <a href="https://wa.me/+6285394477173" target="_blank" class="footer-link-wa">+62 853-9447-7173 - Joseph</a>
    <a href="https://wa.me/+6281290845274" target="_blank" class="footer-link-wa">+62 812-9084-5274 - Euginio</a>
    <a href="https://wa.me/+6285656789704" target="_blank" class="footer-link-wa">+62 856-5678-9704 - Monic</a>
</div>
<div class="footer-right">
    <div class="footer-title">Journal</div>
    <a href="/view" target="_self" class="footer-link">View</a>
</div>
""",
    unsafe_allow_html=True,
)
