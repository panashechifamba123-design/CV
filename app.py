import json
import streamlit as st

from utils.file_parsers import extract_text_from_upload
from utils.job_parser import fetch_job_posting
from utils.llm import call_llm
from utils.scoring import build_tailored_cv, create_change_log, score_match
from utils.text_tools import clean_text

st.set_page_config(page_title="CV Tailor AI", page_icon="📄", layout="wide")

st.title("📄 CV Tailor AI")

mode = st.sidebar.radio("Mode", ["Local", "LLM"])

job_url = st.text_input("Job URL")
job_text_manual = st.text_area("Or paste job description")

uploaded_cv = st.file_uploader("Upload CV", type=["pdf","docx","txt"])
cv_text_manual = st.text_area("Or paste CV")

if st.button("Run"):
    job_text = job_text_manual or fetch_job_posting(job_url)
    cv_text = cv_text_manual or extract_text_from_upload(uploaded_cv)

    job_text = clean_text(job_text)
    cv_text = clean_text(cv_text)

    match_score, strengths, gaps, missing = score_match(job_text, cv_text)
    tailored = build_tailored_cv(job_text, cv_text)

    st.metric("Match Score", f"{match_score}%")
    st.text_area("Tailored CV", tailored, height=400)
