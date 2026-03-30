# AI Resume Analyzer

## Overview

This project is an AI-powered resume analyzer that compares a candidate's resume with a job description using a Large Language Model.

It provides:

- Match score
- Missing skills
- Suggestions for improvement

---

## Features

- Resume vs Job Description comparison
- Skill gap analysis
- AI-generated suggestions
- Simple Streamlit interface

---

## Tech Stack

- Python
- OpenAI API
- Streamlit
- LLM / Prompt Engineering

---

## Project Structure

```text
ai-resume-analyzer/
│
├── app.py
├── analyzer.py
├── requirements.txt
└── README.md
```

---

## How to Run

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Run the application:

```bash
streamlit run app.py
```

---

## Sample Output

```text
Match Score: 78

Missing Skills:
- SQLAlchemy
- AWS Lambda
- CI/CD

Suggestions:
- Add backend API experience
- Highlight cloud deployment work
- Mention ETL and data pipeline projects
```

---

## Author

Sree Sravya Nimmagadda
