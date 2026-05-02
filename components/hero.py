import streamlit as st

# Bagian hero utama (landing section)
# Ubah text di sini jika ingin mengganti headline

def render_hero():
    st.markdown("""
    <div class='hero'>
        <div class='hero-content'>
            <div class='icon'>⬜</div>
            <h1>Medical Health Assistant</h1>
            <p>Your page content will appear here.</p>
            <button class='cta'>Pake Jo</button>
        </div>
    </div>
    """, unsafe_allow_html=True)