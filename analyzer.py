from openai import OpenAI

client = OpenAI()

def analyze_resume(resume_text, job_description):
    prompt = f"""
    Analyze the following resume against the job description.

    Resume:
    {resume_text}

    Job Description:
    {job_description}

    Give:
    1. Match Score (0-100)
    2. Missing Skills
    3. Suggestions to improve
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content
