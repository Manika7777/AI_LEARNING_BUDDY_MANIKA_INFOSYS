import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# ----------------------------
# Page Configuration
# ----------------------------
st.set_page_config(
    page_title="AI Learning Buddy Manika",
    page_icon="🎓",
    layout="centered"
)

# ----------------------------
# Load API Key
# ----------------------------
load_dotenv()

api_key = None

# Try Streamlit Secrets first
try:
    api_key = st.secrets["GEMINI_API_KEY"]
except Exception:
    pass

# If not found, use local .env
if not api_key:
    api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("❌ Gemini API Key not found!")
    st.info(
        "For local use, create a .env file.\n"
        "For Streamlit Cloud, add GEMINI_API_KEY in App Settings → Secrets."
    )
    st.stop()

# Configure Gemini
genai.configure(api_key=api_key)

# Load Gemini Model
model = genai.GenerativeModel("gemini-2.5-flash")

# ----------------------------
# Custom CSS
# ----------------------------
st.markdown("""
<style>

.stApp{
    background: linear-gradient(to right,#eef2ff,#f9fbff);
}

.main-title{
    text-align:center;
    font-size:42px;
    font-weight:700;
    color:#2c3e50;
}

.sub-title{
    text-align:center;
    font-size:18px;
    color:#666;
    margin-bottom:30px;
}

.stTextInput input{
    border-radius:10px;
    border:2px solid #4F8BF9;
}

.stSelectbox div[data-baseweb="select"]{
    border-radius:10px;
}

.stButton > button{
    width:100%;
    background:linear-gradient(90deg,#4F8BF9,#6C63FF);
    color:white;
    border:none;
    border-radius:10px;
    height:50px;
    font-size:18px;
    font-weight:bold;
}

.stButton > button:hover{
    background:linear-gradient(90deg,#3d73d9,#5148ff);
}

.response-card{
    background:white;
    padding:25px;
    border-radius:15px;
    box-shadow:0px 4px 15px rgba(0,0,0,0.1);
    margin-top:20px;
}

.footer{
    text-align:center;
    color:gray;
    margin-top:40px;
    font-size:15px;
}

</style>
""", unsafe_allow_html=True)

# ----------------------------
# Sidebar
# ----------------------------
with st.sidebar:

    st.title("🎓 AI Learning Buddy Manika")

    st.markdown("---")

    st.markdown("""
### Features

✅ Explain Concepts

✅ Real-Life Examples

✅ Generate Quiz

✅ Ask Anything

---

### Built With

- Python
- Streamlit
- Google Gemini AI

---

Created by **Manika Sarkar**
""")

# ----------------------------
# Header
# ----------------------------
st.markdown("""
<div class='main-title'>
🎓 AI Learning Buddy Manika
</div>

<div class='sub-title'>
Learn Today. Lead Tomorrow.
</div>
""", unsafe_allow_html=True)

# ----------------------------
# User Input
# ----------------------------
topic = st.text_input("📖 Enter a Topic")

option = st.selectbox(
    "🎯 Choose Activity",
    [
        "Explain Concept",
        "Real-Life Example",
        "Generate Quiz",
        "Ask Anything"
    ]
)

# ----------------------------
# Generate
# ----------------------------
if st.button("🚀 Generate"):

    if not topic.strip():
        st.warning("⚠️ Please enter a topic.")

    else:

        if option == "Explain Concept":
            prompt = f"Explain {topic} in simple language for a beginner."

        elif option == "Real-Life Example":
            prompt = f"Give one simple real-life example of {topic}."

        elif option == "Generate Quiz":
            prompt = f"Create 5 multiple-choice questions on {topic} with answers."

        else:
            prompt = topic

        try:

            with st.spinner("🤖 AI is generating your response..."):

                response = model.generate_content(
                    prompt,
                    request_options={"timeout": 30}
                )

            st.markdown("<div class='response-card'>", unsafe_allow_html=True)

            st.subheader("🤖 AI Response")

            st.write(response.text)

            st.markdown("</div>", unsafe_allow_html=True)

            st.success("✅ Response generated successfully!")

        except Exception as e:

            st.error("❌ Unable to generate response.")
            st.exception(e)

# ----------------------------
# Footer
# ----------------------------
st.markdown("""
<div class='footer'>
Made with ❤️ by <b>Manika Sarkar</b>
</div>
""", unsafe_allow_html=True)