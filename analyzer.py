from sentence_transformers import SentenceTransformer, util

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Predefined skills list
SKILLS = [
    "Python",
    "AWS",
    "Machine Learning",
    "Deep Learning",
    "Data Pipelines",
    "TensorFlow",
    "Scikit-learn",
    "NLP",
    "SQL",
    "Streamlit",
    "Data Analysis",
    "Feature Engineering",
    "Model Deployment"
]

def analyze_resume(resume_text, job_description):
    # Convert texts to embeddings
    resume_embedding = model.encode(resume_text, convert_to_tensor=True)
    jd_embedding = model.encode(job_description, convert_to_tensor=True)

    # Overall similarity
    score = util.cos_sim(resume_embedding, jd_embedding).item()
    match_score = round(score * 100, 2)

    matched_skills = []
    missing_skills = []

    # Check each skill
    for skill in SKILLS:
        skill_embedding = model.encode(skill, convert_to_tensor=True)

        jd_score = util.cos_sim(jd_embedding, skill_embedding).item()
        resume_score = util.cos_sim(resume_embedding, skill_embedding).item()

        # If skill is important in job
        if jd_score > 0.30:
            if resume_score > 0.30:
                matched_skills.append(skill)
            else:
                missing_skills.append(skill)

    return {
        "match_score": match_score,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "suggestions": "Add missing technical skills and align your resume with the job description."
    }
