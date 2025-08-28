# file: builder/form_handler.py

import streamlit as st
import base64
from .pdf_generator import generate_pdf

def get_pdf_download_link(pdf_bytes, filename="resume.pdf"):
    """Generates a styled download link for the PDF."""
    b64 = base64.b64encode(pdf_bytes).decode()
    return f'<a href="data:application/octet-stream;base64,{b64}" download="{filename}" class="download-link">Download Your Resume PDF</a>'

def handle_resume_form():
    """Handles the dynamic form for building a resume."""
    # Initialize session state for all sections if they don't exist
    if 'work_experience' not in st.session_state:
        st.session_state.work_experience = [{'job_title': '', 'company': '', 'duration': '', 'description': ''}]
    if 'education' not in st.session_state:
        # ADDED: 'cgpa' field
        st.session_state.education = [{'degree': '', 'institution': '', 'year': '', 'cgpa': ''}]
    if 'projects' not in st.session_state:
        # ADDED: 'github_link' field
        st.session_state.projects = [{'project_name': '', 'live_link': '', 'github_link': '', 'description': ''}]
    if 'certifications' not in st.session_state:
        st.session_state.certifications = [{'cert_name': '', 'issuing_org': '', 'date': ''}]

    st.header("Personal Details")
    st.text_input("Full Name", key="full_name")
    st.text_input("Current Job Title (e.g., Senior Accountant)", key="job_title")
    st.text_input("Email", key="email")
    st.text_input("Phone Number", key="phone")
    st.text_input("LinkedIn Profile URL", key="linkedin")
    
    st.text_area("Professional Summary", key="summary")
    st.text_area(
        "Skills (comma-separated)",
        key="skills",
        placeholder="e.g., Python, Project Management, Figma, Public Speaking"
    )
    st.markdown("---")

    st.header("Work Experience")
    for i, job in enumerate(st.session_state.work_experience):
        cols = st.columns((3, 3, 2, 1))
        job['job_title'] = cols[0].text_input("Job Title", value=job.get('job_title', ''), key=f"job_title_{i}")
        job['company'] = cols[1].text_input("Company", value=job.get('company', ''), key=f"company_{i}")
        job['duration'] = cols[2].text_input("Duration", value=job.get('duration', ''), key=f"duration_{i}")
        if cols[3].button("➖", key=f"remove_job_{i}", help="Remove this experience"):
            st.session_state.work_experience.pop(i)
            st.rerun()
        job['description'] = st.text_area("Description (use new lines for bullet points)", value=job.get('description', ''), key=f"job_desc_{i}")
        st.markdown("---")
    if st.button("➕ Add Experience"):
        st.session_state.work_experience.append({'job_title': '', 'company': '', 'duration': '', 'description': ''})
        st.rerun()

    st.header("Education")
    for i, edu in enumerate(st.session_state.education):
        cols = st.columns((4, 4, 2, 2, 1))
        edu['degree'] = cols[0].text_input("Degree/Certificate", value=edu.get('degree', ''), key=f"degree_{i}")
        edu['institution'] = cols[1].text_input("Institution", value=edu.get('institution', ''), key=f"institution_{i}")
        edu['year'] = cols[2].text_input("Year", value=edu.get('year', ''), key=f"year_{i}")
        # ADDED: CGPA input field
        edu['cgpa'] = cols[3].text_input("CGPA (Optional)", value=edu.get('cgpa', ''), key=f"cgpa_{i}")
        if cols[4].button("➖", key=f"remove_edu_{i}", help="Remove this entry"):
            st.session_state.education.pop(i)
            st.rerun()
    if st.button("➕ Add Education"):
        st.session_state.education.append({'degree': '', 'institution': '', 'year': '', 'cgpa': ''})
        st.rerun()

    st.header("Projects")
    for i, proj in enumerate(st.session_state.projects):
        cols = st.columns((4, 4, 1))
        proj['project_name'] = cols[0].text_input("Project Name", value=proj.get('project_name', ''), key=f"proj_name_{i}")
        # ADDED: GitHub Link field
        proj['github_link'] = cols[1].text_input("GitHub Link (Optional)", value=proj.get('github_link', ''), key=f"proj_github_{i}")
        if cols[2].button("➖", key=f"remove_proj_{i}", help="Remove this project"):
            st.session_state.projects.pop(i)
            st.rerun()
        proj['live_link'] = st.text_input("Live Demo Link (Optional)", value=proj.get('live_link', ''), key=f"proj_live_{i}")
        proj['description'] = st.text_area("Project Description", value=proj.get('description', ''), key=f"proj_desc_{i}")
        st.markdown("---")
    if st.button("➕ Add Project"):
        st.session_state.projects.append({'project_name': '', 'live_link': '', 'github_link': '', 'description': ''})
        st.rerun()

    st.header("Certifications")
    for i, cert in enumerate(st.session_state.certifications):
        cols = st.columns((4, 4, 2, 1))
        cert['cert_name'] = cols[0].text_input("Certification Name", value=cert.get('cert_name', ''), key=f"cert_name_{i}")
        cert['issuing_org'] = cols[1].text_input("Issuing Organization", value=cert.get('issuing_org', ''), key=f"cert_org_{i}")
        cert['date'] = cols[2].text_input("Date Obtained", value=cert.get('date', ''), key=f"cert_date_{i}")
        if cols[3].button("➖", key=f"remove_cert_{i}", help="Remove this certification"):
            st.session_state.certifications.pop(i)
            st.rerun()
    if st.button("➕ Add Certification"):
        st.session_state.certifications.append({'cert_name': '', 'issuing_org': '', 'date': ''})
        st.rerun()
    
    st.markdown("---")

    if st.button("Generate Resume PDF", type="primary", use_container_width=True):
        resume_data = {key: st.session_state.get(key, '') for key in st.session_state}
        with st.spinner("Forging your professional resume..."):
            pdf_bytes = generate_pdf(resume_data)
            st.session_state.pdf_link = get_pdf_download_link(pdf_bytes)

    if 'pdf_link' in st.session_state:
        st.success("Your resume is ready!")
        st.markdown(st.session_state.pdf_link, unsafe_allow_html=True)