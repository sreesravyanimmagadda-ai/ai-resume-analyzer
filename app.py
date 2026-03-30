import streamlit as st
from analyzer import analyze_resume

st.title("AI Resume Analyzer")

resume_text = st.text_area("Paste Resume Text")
job_description = st.text_area("Paste Job Description")

if st.button("Analyze Resume"):
    if resume_text and job_description:
        result = analyze_resume(resume_text, job_description)

        st.write(f"Match Score: {result['match_score']}%")
        st.write("Matched Skills:", result["matched_skills"])
        st.write("Missing Skills:", result["missing_skills"])
        st.write("Suggestions:", result["suggestions"])
    else:
        st.warning("Please paste both resume text and job description.")
