from reviewer.resume_parser import extract_text_from_pdf
from insights.utils import clean_resume_text, extract_section_blocks

# Predefined keywords per section
SECTION_KEYWORDS = {
    "Education": ["bachelor", "university", "degree", "gpa", "college", "computer science"],
    "Experience": ["internship", "developed", "built", "collaborated", "project", "managed"],
    "Skills": ["python", "django", "sql", "html", "css", "machine learning", "git", "linux"],
    "Projects": ["chatbot", "web app", "resume builder", "automation", "dashboard", "ai", "ml"]
}

def extract_section_wise_keywords(resume_text: str):
    cleaned_resume = clean_resume_text(resume_text)
    sections = extract_section_blocks(cleaned_resume)

    found_keywords = {}
    missing_keywords = {}

    for section, keywords in SECTION_KEYWORDS.items():
        section_text = sections.get(section.lower(), "")
        present = [kw for kw in keywords if kw in section_text]
        missing = [kw for kw in keywords if kw not in section_text]
        found_keywords[section] = present
        missing_keywords[section] = missing

    return found_keywords, missing_keywords
