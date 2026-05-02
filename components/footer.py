import streamlit as st

# Footer utama

def render_footer():
    st.markdown("""
    <div class='footer'>
        <div class='footer-left'>
            <!-- Section newsletter -->
            <h2>XTRACT</h2>
            <p>Automate Smarter, Optimize Faster, and Grow Stronger.</p>
            <input placeholder='name@email.com'/>
            <button>Subscribe</button>
        </div>
        <div class='footer-center'>
            <!-- Section navigation links -->
            <h4>Links</h4>
            <p>Services</p>
            <p>Process</p>
            <p>Pricing</p>
        </div>
        <div class='footer-right'>
            <!-- Section social media -->
            <h4>Socials</h4>
            <p>Instagram</p>
            <p>LinkedIn</p>
            <p>Twitter</p>
        </div>
    </div>
    """, unsafe_allow_html=True)