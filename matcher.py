def calculate_skill_match(resume_skills, jd_skills):
    if not jd_skills:
        return 0

    matched = set(resume_skills) & set(jd_skills)
    score = (len(matched) / len(jd_skills)) * 100

    return round(score, 2), list(matched)
