import streamlit as st
from utils.navigation import navigate

# Fungsi untuk menampilkan navbar utama
# Sudah diperbaiki agar stabil di Streamlit (tidak sensitif whitespace)

def render_navbar():
    st.markdown("""
    <div class="navbar">
        <div class="nav-left">
            <span class="logo-icon">⬛</span>
            <span class="logo-text">XTRACT</span>
        </div>
        <div class="nav-right">
            <span class="nav-item">About</span>
            <span class="nav-item">Contact</span>
            <span class="nav-cta">Book a call</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Navigation buttons (logic layer)
    cols = st.columns([2,2,2,2,3])

    with cols[0]:
        if st.button("Home", key="nav_home"):
            navigate("home")

    with cols[1]:
        if st.button("About", key="nav_about"):
            navigate("about")

    with cols[2]:
        if st.button("Blog", key="nav_blog"):
            navigate("blog")

    with cols[3]:
        if st.button("Contact", key="nav_contact"):
            navigate("contact")

    with cols[4]:
        st.markdown('<div class="nav-button-wrapper"><button class="cta">Book a call</button></div>', unsafe_allow_html=True)