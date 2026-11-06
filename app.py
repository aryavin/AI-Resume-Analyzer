import streamlit as st
from pdf_reader import extract_text
from analyzer import analyze_resume


# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Vineet AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)


# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

    /* Main background */
    .stApp {
        background: linear-gradient(135deg, #0f172a, #111827, #1e1b4b);
        color: white;
    }

    /* Main container */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 1200px;
    }

    /* Header */
    .main-title {
        font-size: 42px;
        font-weight: 800;
        text-align: center;
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        color: #cbd5e1;
        font-size: 17px;
        margin-bottom: 35px;
    }

    /* Cards */
    .card {
        background: rgba(255,255,255,0.07);
        border: 1px solid rgba(255,255,255,0.12);
        border-radius: 18px;
        padding: 25px;
        margin-bottom: 20px;
        backdrop-filter: blur(10px);
    }

    .card-title {
        font-size: 22px;
        font-weight: 700;
        margin-bottom: 10px;
    }

    /* Upload box */
    [data-testid="stFileUploader"] {
        background: rgba(255,255,255,0.06);
        border-radius: 15px;
        padding: 15px;
        border: 1px dashed #6366f1;
    }

    /* Buttons */
    .stButton > button {
        width: 100%;
        border-radius: 12px;
        padding: 12px;
        font-size: 17px;
        font-weight: 700;
        border: none;
        background: linear-gradient(90deg, #6366f1, #8b5cf6);
        color: white;
        transition: 0.3s;
    }

    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0px 8px 25px rgba(99,102,241,0.35);
    }

    /* Download button */
    .stDownloadButton > button {
        width: 100%;
        border-radius: 12px;
        font-weight: 600;
    }

    /* Report */
    .report-box {
        background: rgba(15,23,42,0.85);
        border: 1px solid rgba(139,92,246,0.35);
        border-radius: 18px;
        padding: 30px;
        margin-top: 20px;
    }

    /* Footer */
    .footer {
        text-align: center;
        color: #94a3b8;
        margin-top: 50px;
        font-size: 14px;
    }

</style>
""", unsafe_allow_html=True)


# ---------------- HEADER ----------------

st.markdown(
    '<div class="main-title">🤖 AI Resume Analyzer</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Analyze your resume with AI and get ATS insights, skills, weaknesses & job recommendations.'
    '</div>',
    unsafe_allow_html=True
)


# ---------------- FEATURES ----------------

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="card">
        <div class="card-title">🎯 ATS Score</div>
        <div>Check how ATS-friendly your resume is.</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <div class="card-title">💡 AI Insights</div>
        <div>Find strengths, weaknesses and missing skills.</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card">
        <div class="card-title">💼 Job Roles</div>
        <div>Get suitable job role recommendations.</div>
    </div>
    """, unsafe_allow_html=True)


# ---------------- UPLOAD ----------------

st.markdown("""
<div class="card">
<div class="card-title">📄 Upload Your Resume</div>
</div>
""", unsafe_allow_html=True)

uploaded_file = st.file_uploader(
    "Choose your resume (PDF)",
    type=["pdf"],
    label_visibility="collapsed"
)


# ---------------- ANALYSIS ----------------

if uploaded_file:

    with st.spinner("📖 Reading resume..."):
        resume = extract_text(uploaded_file)

    st.success("✅ Resume uploaded and read successfully!")

    st.markdown("### 🚀 Ready to Analyze?")

    if st.button("🔍 Analyze Resume"):

        with st.spinner("🤖 AI is analyzing your resume..."):

            result = analyze_resume(resume)

        st.success("🎉 Resume analysis completed!")

        # ---------------- REPORT ----------------

        st.markdown("""
        <div class="report-box">
        <h2>📊 Resume Analysis Report</h2>
        </div>
        """, unsafe_allow_html=True)

        st.markdown(result)

        # ---------------- DOWNLOAD ----------------

        st.download_button(
            "📥 Download Analysis Report",
            result,
            file_name="resume_analysis.txt",
            mime="text/plain"
        )


# ---------------- FOOTER ----------------

st.markdown("""
<div class="footer">
    Built with ❤️ using Python • Streamlit • Ollama • Gemma
    <br>
    © 2026 Vineet AI Resume Analyzer
</div>
""", unsafe_allow_html=True)