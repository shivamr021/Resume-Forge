# 🧠 AI Resume Builder + ATS Reviewer

An intelligent web app built using **Streamlit** that allows users to:

1. ✅ **Build professional resumes** from structured form inputs  
2. 📊 **Evaluate resumes against job descriptions** using ATS-style keyword scoring  
3. 🧠 **Get personalized suggestions** to improve resumes based on missing keywords and formatting insights

---

## 🚀 Features

### 📝 Tab 1: Resume Builder
- Dynamic multi-entry **education section** (with Add/Remove functionality)
- Sections for **basic info, experience, projects, skills, volunteering, hobbies, certifications**
- Bullet-point formatting support for clarity
- Generates a **PDF resume** using ReportLab
- PDF filename generated as `firstname_lastname_resume.pdf`

### 📊 Tab 2: ATS Score Review
- Upload your resume PDF
- Paste job description (optional)
- Calculates **ATS match score** based on keyword overlap
- Handles fallback mode if JD not provided

### 🧠 Tab 3: Resume Suggestions
- Smart analysis of resume keywords grouped by sections:
  - ✅ Found keywords
  - ❌ Missing keywords with actionable advice
- Keywords shown in collapsible expanders for better readability

---

## 📁 Folder Structure

```
.
├── builder/                    # Resume Builder logic
│   ├── form_fields.py         # Form UI components (Basic Info, Projects, Skills etc.)
│   ├── form_handler.py        # Main handler that calls all form sections
│   ├── pdf_generator.py       # Resume PDF generation logic
│   └── styles.py              # Custom CSS styling for better UI
│
├── reviewer/                   # Resume & JD parsing + ATS scoring
│   ├── resume_parser.py       # Extracts text from PDF resumes
│   ├── ats_scoring.py         # Calculates ATS score
│   └── keyword_suggestions.py # (optional/unused)
│
├── insights/                   # Suggestion engine for resume improvement
│   ├── suggestions.py         # Section-wise keyword comparison
│   └── utils.py               # Text cleaning and resume helpers
│
├── app.py                     # Main Streamlit entry point
├── requirements.txt           # Python dependencies
└── README.md                  # Project readme (this file)
```

---

## ⚙️ Installation & Run

### 1. Clone the repo
```bash
git clone https://github.com/yourusername/resume-reviewer.git
cd resume-reviewer
```

### 2. Create virtual environment (optional but recommended)
```bash
python -m venv .venv
source .venv/bin/activate  # on Linux/macOS
.venv\Scripts\activate     # on Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the app
```bash
streamlit run app.py
```

The app will be available at `http://localhost:8501`

---

## 🛠️ Tech Stack

- **Python 3.10+**
- **Streamlit** (UI framework)
- **ReportLab** (PDF generation)
- **scikit-learn** (keyword vectorization)
- **fuzzywuzzy / difflib** (keyword matching logic)
- **PyPDF2** (PDF text extraction)

---

## 🎯 How to Use

### Building a Resume
1. Navigate to the **"📝 Build Resume"** tab
2. Fill in your basic information (name, email, phone, LinkedIn, GitHub)
3. Add education entries using the **"➕ Add Education"** button
4. Describe your work experience with bullet points
5. Add project details and skills
6. Optionally fill in volunteering, hobbies, and certifications
7. Click **"📄 Generate Resume"** to download your PDF

### ATS Review
1. Go to the **"📊 ATS Review"** tab
2. Upload your resume PDF
3. Optionally paste a job description
4. Click **"🔍 Analyze Resume"** to get your ATS score
5. Review the keyword analysis and suggestions

### Getting Suggestions
1. Use the **"🧠 Suggestions"** tab after uploading a resume
2. View found keywords grouped by resume sections
3. See missing keywords with actionable advice
4. Use the suggestions to improve your resume

---

## 🔮 Upcoming Features

- [ ] Support for resume templates
- [ ] Export as DOCX format
- [ ] Section reordering functionality
- [ ] Integration with LinkedIn for keyword boosting
- [ ] Multiple resume formats and styles
- [ ] Resume comparison tools

---

## 🤝 Contributing

PRs and issues are welcome! Open a ticket or fork the repo and suggest improvements.

### How to Contribute
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is open-source and available under the MIT License.

---

## 👨‍💻 Author

**Shivam Rathod**

- LinkedIn: [shivamrathod021](https://linkedin.com/in/shivamrathod021)
- GitHub: [shivamr021](https://github.com/shivamr021)

Built with 💡 by Shivam Rathod.

---

## 🙏 Acknowledgments

- Streamlit community for the amazing UI framework
- ReportLab for PDF generation capabilities
- Open-source contributors who made this project possible

---

## 📞 Support

If you have any questions or need help, feel free to:
- Open an issue on GitHub
- Contact me on LinkedIn
- Star the repository if you find it helpful! ⭐
