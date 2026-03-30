def analyze_resume(resume_text, job_description):
    resume_words = set(resume_text.lower().split())
    job_words = set(job_description.lower().split())

    matched_skills = resume_words.intersection(job_words)
    missing_skills = job_words - resume_words

    match_score = len(matched_skills) / len(job_words) * 100 if job_words else 0

    return {
        "match_score": round(match_score, 2),
        "matched_skills": list(matched_skills),
        "missing_skills": list(missing_skills),
        "suggestions": "Improve by adding missing skills and aligning resume with job description."
    }
