import streamlit as st
import streamlit.components.v1 as components
import base64

# ✅ URL of your System Dashboard (the big purple header page)
DASHBOARD_URL = "https://synapse1023-6d63jya1k-utkarsh-s-projects-51b8a251.vercel.app/analytics"

st.set_page_config(
    page_title="Brake Shoe & Brake Pad Portal",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ------------------ Remove Streamlit UI ------------------
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

# ------------------ FILE PATHS (ROOT ONLY) ------------------
LOGO_PATH = "logo.png"
BG_PATH = "abstract-flowing-neon-wave-background_53876-101942.jpg"   # make sure filename matches

# ------------------ LOAD IMAGES ------------------
with open(LOGO_PATH, "rb") as f:
    logo_b64 = base64.b64encode(f.read()).decode()

with open(BG_PATH, "rb") as f:
    bg_b64 = base64.b64encode(f.read()).decode()

# ------------------ LOAD CSS ------------------
with open("styles.css", "r", encoding="utf-8") as f:
    css = f.read()

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

# ------------------ LOAD HTML ------------------
with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# inline logo image
html = html.replace(
    'src="logo.png"',
    f'src="data:image/png;base64,{logo_b64}"'
)

# ------------------ JS: INTERCEPT THE LOGIN FORM ------------------
login_js = f"""
<script>
document.addEventListener('DOMContentLoaded', function() {{
    // select the login form
    var form = document.querySelector('form.login-form');
    if (!form) return;

    form.addEventListener('submit', function(e) {{
        e.preventDefault(); // stop default POST /login

        var emailInput = form.querySelector('input[name="email"]');
        var passwordInput = form.querySelector('input[name="password"]');

        if (!emailInput || !passwordInput) {{
            alert('Login fields not found.');
            return;
        }}

        var userEmail = emailInput.value;
        var userPassword = passwordInput.value;

        var defaultEmail = 'admin@niit.com';
        var defaultPassword = '12345';

        if (userEmail === defaultEmail && userPassword === defaultPassword) {{
            // ✅ Redirect full tab to your dashboard
            window.top.location.href = '{DASHBOARD_URL}';
        }} else {{
            var err = document.getElementById('errorBox');
            if (err) {{
                err.style.display = 'block';
            }} else {{
                alert('Invalid email or password');
            }}
        }}
    }});
}});
</script>
"""

# ------------------ RENDER ------------------
final_html = f"<style>{css}</style>\n{html}\n{login_js}"
components.html(final_html, height=900, scrolling=False)
