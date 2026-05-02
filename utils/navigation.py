import streamlit as st

# Fungsi navigasi antar halaman
def navigate(page_name):
    st.session_state.page = page_name