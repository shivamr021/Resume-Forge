import re
from sklearn.feature_extraction.text import CountVectorizer

def clean_resume_text(text: str) -> str:
    return re.sub(r'\s+', ' ', text).strip().lower()

def extract_keywords(text, top_n=20):
    text = clean_resume_text(text)
    vectorizer = CountVectorizer(stop_words='english', max_features=top_n)
    X = vectorizer.fit_transform([text])
    return vectorizer.get_feature_names_out().tolist()

def extract_section_blocks(text: str) -> dict:
    """
    Splits the resume into sections based on known headers.
    Returns a dictionary: {section_name: text_in_section}
    """
    section_map = {
        "education": "",
        "experience": "",
        "skills": "",
        "projects": ""
    }

    current_section = None
    lines = text.split('\n')
    for line in lines:
        line_clean = line.strip().lower()
        if "education" in line_clean:
            current_section = "education"
        elif "experience" in line_clean or "work history" in line_clean:
            current_section = "experience"
        elif "skill" in line_clean or "technical expertise" in line_clean:
            current_section = "skills"
        elif "project" in line_clean:
            current_section = "projects"
        elif current_section:
            section_map[current_section] += " " + line_clean

    return section_map
