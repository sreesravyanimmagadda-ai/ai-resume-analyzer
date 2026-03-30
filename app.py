if st.button("Analyze Resume"):
    result = analyze_resume(resume_text, job_description)

    st.write(f"Match Score: {result['match_score']}%")
    st.write("Matched Skills:", result['matched_skills'])
    st.write("Missing Skills:", result['missing_skills'])
    st.write("Suggestions:", result['suggestions'])
