import streamlit as st
from resume_parser import extract_text_from_pdf
from skill_extracter import extract_skills
from matcher import calculate_skill_match

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="centered"
)

st.markdown(
    """
    <h1 style="text-align:center;">📄 AI Resume Analyzer</h1>
    <p style="text-align:center; color:grey;">
    ATS-style resume and job description matching
    </p>
    """,
    unsafe_allow_html=True
)

st.divider()

mode = st.radio(
    "Choose an option",
    ["Analyze Resume", "About Project"],
    horizontal=True
)

if mode == "Analyze Resume":
    st.markdown("## Upload Resume")
    resume_file = st.file_uploader(
        "Upload resume (PDF only)",
        type=["pdf"],
        label_visibility="collapsed"
    )

    st.markdown("## Job Description")
    job_description = st.text_area(
        "Paste job description here",
        height=180
    )

    if resume_file and job_description:
        resume_text = extract_text_from_pdf(resume_file)

        if resume_text.strip() == "":
            st.error("Unable to extract text from this resume.")
        else:
            resume_skills = extract_skills(resume_text)
            jd_skills = extract_skills(job_description)
            match_score, matched_skills = calculate_skill_match(
                resume_skills, jd_skills
            )
            missing_skills = set(jd_skills) - set(resume_skills)

            if match_score >= 80:
                color, label = "green", "Excellent Match"
            elif match_score >= 50:
                color, label = "orange", "Moderate Match"
            else:
                color, label = "red", "Low Match"

            st.divider()
            st.markdown("## Match Result")
            st.markdown(
                f"<h2 style='color:{color};'>{match_score}% — {label}</h2>",
                unsafe_allow_html=True
            )
            st.progress(int(match_score))
            st.divider()

            col1, col2 = st.columns(2)

            with col1:
                st.markdown("### Matched Skills")
                if matched_skills:
                    for skill in matched_skills:
                        st.success(skill)
                else:
                    st.info("No matched skills found")

            with col2:
                st.markdown("### Missing Skills")
                if missing_skills:
                    for skill in missing_skills:
                        st.warning(skill)
                else:
                    st.success("No major skills missing")

            with st.expander("View Extracted Resume Text"):
                st.text_area(
                    "Resume Content",
                    resume_text,
                    height=250
                )
    else:
        st.info("Upload a resume and paste a job description to continue.")

else:
    st.markdown("## About This Project")
    st.write(
        """
        This project analyzes resumes against job descriptions using
        skill-based matching logic similar to ATS systems.
        It helps identify matching and missing skills clearly.
        """
    )
