import re
from sklearn.feature_extraction.text import CountVectorizer

from .ats_scoring import clean_text, extract_keywords

def get_suggestions(resume_text: str, job_desc: str) -> dict:
    resume_clean = clean_text(resume_text)
    jd_clean = clean_text(job_desc)

    resume_keywords = set(extract_keywords(resume_clean))
    jd_keywords = set(extract_keywords(jd_clean))

    matched_keywords = sorted(resume_keywords & jd_keywords)
    missing_keywords = sorted(jd_keywords - resume_keywords)

    # Length feedback
    resume_len = len(resume_clean.split())
    if resume_len < 100:
        length_feedback = "Your resume is too short. Consider adding more details."
    elif resume_len > 800:
        length_feedback = "Your resume is quite long. Try making it more concise."
    else:
        length_feedback = "Resume length looks good."

    # Basic grammar/filler check
    filler_words = ["very", "really", "etc", "etc.", "thing", "stuff"]
    grammar_flags = [w for w in filler_words if w in resume_clean]

    # Section suggestions (heuristics)
    section_hints = []
    if "project" in missing_keywords:
        section_hints.append("Consider adding a Projects section.")
    if "internship" in missing_keywords or "experience" in missing_keywords:
        section_hints.append("Include relevant experience or internships.")
    if "skill" in missing_keywords:
        section_hints.append("Make sure to include a Skills section.")

    return {
        "matched_keywords": matched_keywords,
        "missing_keywords": missing_keywords,
        "length_feedback": length_feedback,
        "grammar_flags": grammar_flags,
        "section_hints": section_hints,
    }
