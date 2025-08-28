# file: reviewer/ats_scoring.py

import streamlit as st
from sentence_transformers import SentenceTransformer, util
from keybert import KeyBERT

# Preload SBERT model once (used by both KeyBERT and for matching)
try:
    SBERT_MODEL = SentenceTransformer("all-MiniLM-L6-v2")
    # Initialize KeyBERT with the SBERT model
    KEYBERT_MODEL = KeyBERT(model=SBERT_MODEL)
except Exception as e:
    st.error(f"Error loading sentence model: {e}")
    SBERT_MODEL = None
    KEYBERT_MODEL = None

def get_key_skills_from_jd_local(job_description: str) -> list:
    """Uses a local KeyBERT model to extract key skills and phrases."""
    if not KEYBERT_MODEL:
        return []
    try:
        keywords = KEYBERT_MODEL.extract_keywords(
            job_description,
            keyphrase_ngram_range=(1, 3), # Find skills up to 3 words long
            stop_words='english',
            top_n=15 # Extract the top 15 skills
        )
        # KeyBERT returns a list of tuples (keyword, score), we just need the keyword
        return [kw[0] for kw in keywords]
    except Exception as e:
        st.error(f"Error extracting local keywords: {e}")
        return []

def calculate_ats_score(resume_text: str, job_description: str):
    """
    Calculates ATS score using a LOCAL keyword extraction model.
    NO API CALLS are made in this function.
    """
    if not job_description:
        return {"score": 0, "matched_skills": [], "missing_skills": [], "feedback": "Please provide a job description."}

    if not SBERT_MODEL:
        return {"score": 0, "matched_skills": [], "missing_skills": [], "feedback": "Sentence model not loaded."}
        
    jd_skills = get_key_skills_from_jd_local(job_description)
    if not jd_skills:
        return {"score": 0, "matched_skills": [], "missing_skills": [], "feedback": "Could not extract skills from the job description."}
    
    resume_embedding = SBERT_MODEL.encode(resume_text)
    matched_skills = []
    missing_skills = []
    
    for skill in jd_skills:
        skill_embedding = SBERT_MODEL.encode(skill)
        similarity = util.pytorch_cos_sim(skill_embedding, resume_embedding).item()
        
        if similarity > 0.4:
            matched_skills.append(skill)
        else:
            missing_skills.append(skill)
            
    score = (len(matched_skills) / len(jd_skills)) * 100 if jd_skills else 0
    
    return {
        "score": int(score),
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "feedback": f"Your resume covers {len(matched_skills)} of the {len(jd_skills)} key skills identified in the job description."
    }