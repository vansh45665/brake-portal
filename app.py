import streamlit as st
import streamlit.components.v1 as components
import base64

st.set_page_config(
    page_title="Brake Shoe & Brake Pad Portal",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ---- Remove Streamlit chrome and padding ----
st.markdown("""
<style>
html, body, [class*="css"] {
    margin: 0 !important;
    padding: 0 !important;
}
.stApp {
    margin: 0 !important;
    padding: 0 !important;
    background: transparent !important;
}
.block-container {
    margin: 0 !important;
    padding: 0 !important;
    max-width: 100% !important;
}
header {visibility: hidden;}
footer {visibility: hidden;}
#MainMenu {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# ---------- 1) Filenames IN REPO ROOT ----------
LOGO_PATH = "logo.png"  # must exist in the repo root

# 🔴 VERY IMPORTANT:
# Go to your repo, copy the exact name of your neon background file
# (the one starting with "abstract-flowing-neon-wave-...")
BG_PATH = "abstract-flowing-neon-wave-background_53876-101942.jpg"

# ---------- 2) Load images as Base64 ----------
with open(LOGO_PATH, "rb") as f:
    logo_b64 = base64.b64encode(f.read()).decode()

with open(BG_PATH, "rb") as f:
    bg_b64 = base64.b64encode(f.read()).decode()

# ---------- 3) Load CSS ----------
with open("styles.css", "r", encoding="utf-8") as f:
    css = f.read()

# Add neon background via ::before so layout from CSS stays the same
css += f"""
body::before {{
    content: "";
    position: fixed;
    inset: 0;
    z-index: -1;
    background:
        linear-gradient(0deg, rgba(0,0,0,0.55), rgba(0,0,0,0.55)),
        url("data:image/jpeg;base64,{bg_b64}"_
