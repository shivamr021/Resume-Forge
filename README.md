# 🔨 Resume Forge: AI-Powered Resume Builder & Reviewer

**Resume Forge** is an intelligent, all-in-one web application designed to help you build a professional, modern resume and optimize it for Applicant Tracking Systems (ATS) using a sophisticated hybrid AI model.

---

## ✨ Key Features

Resume Forge is built around three core modules, providing a seamless experience from creation to optimization.

### 1. Dynamic Resume Builder

* **Modern Two-Column PDF**: Generate a visually appealing, professional resume in a clean two-column layout that is easy for recruiters to read.
* **Fully Dynamic Form**: Add or remove multiple entries for work experience, education, projects, and certifications on the fly.
* **Comprehensive Fields**: Includes all necessary sections, from personal details and a professional summary to skills, CGPA, and project links (GitHub & Live Demo).
* **Instant PDF Download**: Get a downloadable PDF of your resume as soon as you're done editing.

### 2. AI-Powered ATS Review

* **Specific Job Targeting**: Paste a job description to see how well your resume aligns with the role.
* **Local AI Scoring (Free & Fast)**: Uses a local KeyBERT and SentenceTransformer model to analyze the job description, extract the most critical skills, and perform semantic search on your resume. Provides a quantitative ATS score without any API calls.
* **Skill Gap Analysis**: Instantly see which key skills from the job description are present on your resume and which ones are missing.

### 3. AI Career Coach

* **General Quality Review**: Get a "Resume Quality Score" and actionable feedback on structure, clarity, and impact.
* **In-Depth Suggestions (Powered by Google Gemini)**:

  * *Overall Impression*: Strengths and weaknesses.
  * *Alignment with Job Description*: How well your resume matches a given role.
  * *Action Verb Analysis*: Suggestions for stronger, more impactful verbs.
  * *Content & Clarity*: Tips to refine your descriptions and summaries.

---

## 🛠️ Tech Stack

This project leverages a modern stack of Python libraries for web development, PDF generation, and machine learning.

* **Framework**: [Streamlit](https://streamlit.io/)
* **PDF Generation**: [fpdf2](https://github.com/py-pdf/fpdf2) (with full Unicode and emoji support)
* **AI & Machine Learning**:

  * Generative AI: Google Generative AI SDK (`gemini-1.5-flash-latest`)
  * NLP & Keyword Extraction: `sentence-transformers`, `keybert`
* **Data Visualization**: Plotly
* **File Parsing**: PyPDF2

---

## 🚀 Getting Started

Follow these steps to run the project on your local machine.

### 1. Prerequisites

* Python 3.10 or higher
* An active Google Gemini API key ([Get one here](https://aistudio.google.com/))

### 2. Clone the Repository

```bash
git clone https://github.com/shivamr021/Resume-Forge.git
cd Resume-Forge
```

### 3. Create a Virtual Environment

```bash
# For Windows
python -m venv .venv
.\.venv\Scripts\activate

# For macOS/Linux
python3 -m venv .venv
source .venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Set Up Your API Key

Create a secrets file for your API key. This file is included in `.gitignore`.

```bash
mkdir .streamlit
nano .streamlit/secrets.toml
```

Add your key:

```toml
# .streamlit/secrets.toml
GOOGLE_API_KEY = "YOUR_API_KEY_HERE"
```

### 6. Run the Application

```bash
streamlit run app.py
```

Your application will now be running in the browser!

---

## 📈 Project Evolution & Learnings

This project was a journey of continuous improvement, evolving from a simple, rule-based script into a sophisticated hybrid AI application. Key milestones included:

* **Upgrading PDF Generation**: Migrated from `fpdf` to `fpdf2` to solve Unicode and font-embedding issues, enabling a more robust and visually appealing resume design.
* **Securing Credentials**: Implemented secure API key management using Streamlit's `secrets.toml` and a comprehensive `.gitignore` to prevent credential leaks.
* **Implementing a Hybrid AI Model**: Transitioned from a costly, API-only approach to a more efficient hybrid model:

  * Local KeyBERT for high-frequency quantitative ATS scoring.
  * Google Gemini for low-frequency, high-value qualitative feedback.

This balance created a scalable and cost-effective solution.

---

## 👤 Author

**Shivam Rathod**

* GitHub: [shivamr021](https://github.com/shivamr021)
* LinkedIn: [shivamrathod021](https://www.linkedin.com/in/shivamrathod021)
