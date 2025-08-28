import streamlit as st

def show_form_tips():
    """Display helpful tips for users"""
    with st.expander("💡 Tips for a Great Resume", expanded=False):
        st.markdown("""
        **📝 Writing Tips:**
        - Use action verbs (e.g., Developed, Implemented, Led, Managed)
        - Include quantifiable achievements (e.g., "Increased efficiency by 25%")
        - Keep bullet points concise and impactful
        - Use industry-specific keywords relevant to your target role
        
        **🎯 ATS Optimization:**
        - Include relevant keywords from job descriptions
        - Use standard section headings
        - Avoid graphics, tables, or complex formatting
        - Keep your resume to 1-2 pages maximum
        
        **📋 Format Guidelines:**
        - Use bullet points for experience and projects
        - Separate skills with commas
        - Include dates in YYYY format for education
        - Provide specific examples and outcomes
        """)

def basic_fields():
    st.subheader("👤 Basic Information")
    
    # Using columns for better layout
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("Full Name", key="name", placeholder="John Doe")
        email = st.text_input("Email", key="email", placeholder="john.doe@email.com")
        phone = st.text_input("Phone Number", key="phone", placeholder="+1 (555) 123-4567")
        location = st.text_input("Location", key="location", placeholder="City, State, Country")
    with col2:
        title = st.text_input("Professional Title", key="title", placeholder="Software Developer & Cybersecurity Enthusiast")
        linkedin = st.text_input("LinkedIn URL (Optional)", key="linkedin", placeholder="https://linkedin.com/in/johndoe")
        github = st.text_input("GitHub URL (Optional)", key="github", placeholder="https://github.com/johndoe")
        
    return name, email, phone, location, title, linkedin, github

def professional_summary():
    st.subheader("📋 Professional Summary")
    return st.text_area("Write a brief professional summary", key="summary", height=100,
                       placeholder="Software Developer with expertise in full-stack development and hands-on experience in Python development. Seeking challenging software development roles leveraging strong programming foundation and problem-solving skills.")

def education_section():
    st.subheader("🎓 Education")

    # Display education entries
    for idx, entry in enumerate(st.session_state.education_entries):
        with st.container():
            st.markdown("---")
            entry_col1, entry_col2 = st.columns([4, 1])
            with entry_col1:
                st.markdown(f"**Education Entry {idx + 1}**")
            with entry_col2:
                st.markdown("")  # Placeholder for remove button, handled outside form
            col1, col2 = st.columns(2)
            with col1:
                entry["institution"] = st.text_input("Institution", value=entry["institution"], key=f"institution_{idx}")
                entry["degree"] = st.text_input("Degree", value=entry["degree"], key=f"degree_{idx}")
            with col2:
                entry["start"] = st.text_input("Start Year", value=entry["start"], key=f"start_{idx}")
                entry["end"] = st.text_input("End Year", value=entry["end"], key=f"end_{idx}")
            entry["grade"] = st.text_input("Grade/Percentage/CGPA", value=entry["grade"], key=f"grade_{idx}")

def experience_section():
    st.subheader("💼 Professional Experience")

    # Display experience entries
    for idx, entry in enumerate(st.session_state.experience_entries):
        with st.container():
            st.markdown("---")
            entry_col1, entry_col2 = st.columns([4, 1])
            with entry_col1:
                st.markdown(f"**Experience Entry {idx + 1}**")
            with entry_col2:
                st.markdown("")  # Placeholder for remove button, handled outside form
            col1, col2 = st.columns(2)
            with col1:
                entry["job_title"] = st.text_input("Job Title", value=entry["job_title"], key=f"job_title_{idx}")
                entry["company"] = st.text_input("Company/Organization", value=entry["company"], key=f"company_{idx}")
            with col2:
                entry["start_date"] = st.text_input("Start Date (e.g., June 2024)", value=entry["start_date"], key=f"start_date_{idx}")
                entry["end_date"] = st.text_input("End Date (e.g., July 2024 or Present)", value=entry["end_date"], key=f"end_date_{idx}")
            entry["description"] = st.text_area("Job Description (\\n-separated for bullet points)", value=entry["description"], key=f"description_{idx}", height=100,
                                               placeholder="• Developed 15+ Python applications with 25% code efficiency improvement\n• Achieved 100% project delivery rate in 1-month intensive program")

def project_section():
    st.subheader("🚀 Key Projects")

    # Display project entries
    for idx, entry in enumerate(st.session_state.project_entries):
        with st.container():
            st.markdown("---")
            entry_col1, entry_col2 = st.columns([4, 1])
            with entry_col1:
                st.markdown(f"**Project Entry {idx + 1}**")
            with entry_col2:
                st.markdown("")  # Placeholder for remove button, handled outside form
            col1, col2 = st.columns(2)
            with col1:
                entry["title"] = st.text_input("Project Title", value=entry["title"], key=f"project_title_{idx}")
                entry["technologies"] = st.text_input("Technologies Used", value=entry["technologies"], key=f"technologies_{idx}")
            with col2:
                entry["link"] = st.text_input("Project Link (Optional)", value=entry["link"], key=f"project_link_{idx}")
            entry["description"] = st.text_area("Project Description (\\n-separated for bullet points)", value=entry["description"], key=f"project_desc_{idx}", height=100,
                                               placeholder="• Developed full-stack platform with shopping cart and user authentication\n• Achieved 95% mobile compatibility with Django MVT architecture")

def skills_section():
    st.subheader("🧠 Technical Skills")
    
    col1, col2 = st.columns(2)
    with col1:
        programming = st.text_input("Programming Languages", key="programming_skills", placeholder="Python, JavaScript, C/C++, SQL")
        web_dev = st.text_input("Web Development", key="web_dev_skills", placeholder="Django, HTML5, CSS3, Bootstrap")
        data_analysis = st.text_input("Data Analysis", key="data_analysis_skills", placeholder="Pandas, NumPy, Matplotlib, Seaborn")
    with col2:
        tools = st.text_input("Tools", key="tools_skills", placeholder="Git, GitHub, Data Structures & Algorithms")
        cybersecurity = st.text_input("Cybersecurity (Optional)", key="cybersecurity_skills", placeholder="Security Frameworks, Risk Management")
        other_skills = st.text_input("Other Skills (Optional)", key="other_skills", placeholder="Machine Learning, Cloud Computing")
    
    return {
        "Programming": programming,
        "Web Development": web_dev,
        "Data Analysis": data_analysis,
        "Tools": tools,
        "Cybersecurity": cybersecurity,
        "Other Skills": other_skills
    }

def additional_sections():
    st.subheader("📌 Additional Sections (Optional)")

    col1, col2 = st.columns(2)
    with col1:
        volunteering = st.text_area("Volunteering / Extra-curricular Activities", key="volunteering", height=100)
        certifications = st.text_area("Certifications / Courses", key="certifications", height=100)
    with col2:
        hobbies = st.text_input("Hobbies (comma separated)", key="hobbies", placeholder="e.g., Reading, Hiking, Photography")
    return volunteering, hobbies, certifications
