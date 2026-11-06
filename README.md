# 🤖 AI Resume Analyzer

A Streamlit app that analyzes your resume using a local LLM (Ollama + Gemma) and gives you an ATS score, strengths, weaknesses, missing skills, job role suggestions and interview questions.

## Features
- 🎯 ATS score out of 100
- 💡 Strengths, weaknesses and missing skills
- 💼 Suitable job roles
- ❓ Interview questions with sample answers
- 📥 Download the report as a text file

## Tech Stack
Python, Streamlit, Ollama (gemma3:270m), PyPDF2

## Prerequisites
1. Python 3.9+
2. [Ollama](https://ollama.com/download) installed and running

## Setup

```bash
git clone https://github.com/<your-username>/Ai_Resume_analyzer.git
cd Ai_Resume_analyzer

python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux

pip install -r requirements.txt

ollama pull gemma3:270m

streamlit run app.py
```

## Usage
1. Upload your resume (PDF)
2. Click **Analyze Resume**
3. Read the report or download it

## Note
This app runs locally and needs Ollama running in the background. Resume data never leaves your machine.

## Author
Vineet