def extract_skills(text):
    skills_db = [
        "python", "java", "c++", "sql",
        "machine learning", "data analysis",
        "nlp", "flask", "fastapi", "streamlit",
        "pandas", "numpy", "scikit-learn", "github"
    ]

    text = text.lower()
    found = set()

    for skill in skills_db:
        if skill in text:
            found.add(skill)

    return sorted(found)
