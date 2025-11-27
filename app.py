import streamlit as st
import streamlit.components.v1 as components
import base64

st.set_page_config(
    page_title="Brake Shoe & Brake Pad Portal",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Remove Streamlit chrome and padding
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

# ---- Load images as Base64 ----
with open("New folder/logo.png", "rb") as f:
    logo_b64 = base64.b64encode(f.read()).decode()

with open("New folder/abstract-flowing-neon-wave-background_53876-101942.jpg", "rb") as f:
    bg_b64 = base64.b64encode(f.read()).decode()

# ---- Load original CSS ----
with open("styles.css", "r", encoding="utf-8") as f:
    css = f.read()

# Add background overlay using pseudo-element so layout is unchanged
css += f"""
body::before {{
    content: "";
    position: fixed;
    inset: 0;
    z-index: -1;
    background:
        linear-gradient(0deg, rgba(0,0,0,0.55), rgba(0,0,0,0.55)),
        url("data:image/jpeg;base64,{bg_b64}") no-repeat center center fixed;
    background-size: cover;
}}
"""

# ---- Load HTML ----
with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Replace logo path by Base64 data URL
html = html.replace(
    'src="logo.png"',
    f'src="data:image/png;base64,{logo_b64}"'
).replace(
    'src="./New folder/logo.png"',
    f'src="data:image/png;base64,{logo_b64}"'
)

# ---- Combine and render ----
final_html = f"<style>{css}</style>\n{html}"
components.html(final_html, height=900, scrolling=False)
