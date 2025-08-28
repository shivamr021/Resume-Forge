import streamlit as st
import base64
# Import the generator function from our new module
from .pdf_generator import generate_pdf

def get_pdf_download_link(pdf_bytes, filename="resume.pdf"):
    """Generates a link to download the PDF."""
    b64 = base64.b64encode(pdf_bytes).decode()
    return f'<a href="data:application/octet-stream;base64,{b64}" download="{filename}" style="background-color:#FF4B4B;color:white;padding:0.5rem 1rem;border-radius:0.5rem;text-decoration:none;">Download Your Resume PDF</a>'

def handle_resume_form():
    """
    Handles the dynamic form for building a resume.
    All sections are laid out, with a final generate button at the end.
    """
    # Initialize session state for all sections if they don't exist
    if 'work_experience' not in st.session_state:
        st.session_state.work_experience = [{'job_title': '', 'company': '', 'duration': '', 'description': ''}]
    if 'education' not in st.session_state:
        st.session_state.education = [{'degree': '', 'institution': '', 'year': ''}]
    if 'projects' not in st.session_state:
        st.session_state.projects = [{'project_name': '', 'description': '', 'link': ''}]
    if 'certifications' not in st.session_state:
        st.session_state.certifications = [{'cert_name': '', 'issuing_org': '', 'date': ''}]


    # --- Part 1: Personal Details (No longer in a form) ---
    st.header("Personal Details")
    st.text_input("Full Name", key="full_name")
    st.text_input("Current Job Title (e.g., Senior Accountant)", key="job_title") # ADDED THIS LINE
    st.text_input("Email", key="email")
    st.text_input("Phone", key="phone")
    st.text_input("LinkedIn Profile URL", key="linkedin")
    st.text_area("Professional Summary", key="summary")
    st.text_area(
        "Skills (comma-separated)",
        key="skills",
        placeholder="e.g., Python, Project Management, Figma, Public Speaking, Data Analysis"
    )

    st.markdown("---")

    # --- Part 2: Dynamic Sections ---
    st.header("Work Experience")
    for i, job in enumerate(st.session_state.work_experience):
        cols = st.columns((3, 3, 2, 1))
        st.session_state.work_experience[i]['job_title'] = cols[0].text_input("Job Title", value=job['job_title'], key=f"job_title_{i}")
        st.session_state.work_experience[i]['company'] = cols[1].text_input("Company", value=job['company'], key=f"company_{i}")
        st.session_state.work_experience[i]['duration'] = cols[2].text_input("Duration", value=job['duration'], key=f"duration_{i}")
        if cols[3].button("➖", key=f"remove_job_{i}", help="Remove this experience"):
            st.session_state.work_experience.pop(i)
            # Clear the old PDF link when the form is edited
            if 'pdf_link' in st.session_state:
                del st.session_state['pdf_link']
            st.rerun()
        st.session_state.work_experience[i]['description'] = st.text_area("Description", value=job['description'], key=f"job_desc_{i}")
        st.markdown("---")
    if st.button("➕ Add Experience"):
        st.session_state.work_experience.append({'job_title': '', 'company': '', 'duration': '', 'description': ''})
        if 'pdf_link' in st.session_state:
            del st.session_state['pdf_link']
        st.rerun()

    st.header("Education")
    for i, edu in enumerate(st.session_state.education):
        cols = st.columns((4, 4, 2, 1))
        st.session_state.education[i]['degree'] = cols[0].text_input("Degree/Certificate", value=edu['degree'], key=f"degree_{i}")
        st.session_state.education[i]['institution'] = cols[1].text_input("Institution", value=edu['institution'], key=f"institution_{i}")
        st.session_state.education[i]['year'] = cols[2].text_input("Year", value=edu['year'], key=f"year_{i}")
        if cols[3].button("➖", key=f"remove_edu_{i}", help="Remove this education entry"):
            st.session_state.education.pop(i)
            if 'pdf_link' in st.session_state:
                del st.session_state['pdf_link']
            st.rerun()
    if st.button("➕ Add Education"):
        st.session_state.education.append({'degree': '', 'institution': '', 'year': ''})
        if 'pdf_link' in st.session_state:
            del st.session_state['pdf_link']
        st.rerun()

    st.header("Projects")
    for i, proj in enumerate(st.session_state.projects):
        cols = st.columns((4, 4, 1))
        st.session_state.projects[i]['project_name'] = cols[0].text_input("Project Name", value=proj['project_name'], key=f"proj_name_{i}")
        st.session_state.projects[i]['link'] = cols[1].text_input("Project Link", value=proj['link'], key=f"proj_link_{i}")
        if cols[2].button("➖", key=f"remove_proj_{i}", help="Remove this project"):
            st.session_state.projects.pop(i)
            if 'pdf_link' in st.session_state:
                del st.session_state['pdf_link']
            st.rerun()
        st.session_state.projects[i]['description'] = st.text_area("Project Description", value=proj['description'], key=f"proj_desc_{i}")
        st.markdown("---")
    if st.button("➕ Add Project"):
        st.session_state.projects.append({'project_name': '', 'description': '', 'link': ''})
        if 'pdf_link' in st.session_state:
            del st.session_state['pdf_link']
        st.rerun()

    st.header("Certifications")
    for i, cert in enumerate(st.session_state.certifications):
        cols = st.columns((4, 4, 2, 1))
        st.session_state.certifications[i]['cert_name'] = cols[0].text_input("Certification Name", value=cert['cert_name'], key=f"cert_name_{i}")
        st.session_state.certifications[i]['issuing_org'] = cols[1].text_input("Issuing Organization", value=cert['issuing_org'], key=f"cert_org_{i}")
        st.session_state.certifications[i]['date'] = cols[2].text_input("Date Obtained", value=cert['date'], key=f"cert_date_{i}")
        if cols[3].button("➖", key=f"remove_cert_{i}", help="Remove this certification"):
            st.session_state.certifications.pop(i)
            if 'pdf_link' in st.session_state:
                del st.session_state['pdf_link']
            st.rerun()
    if st.button("➕ Add Certification"):
        st.session_state.certifications.append({'cert_name': '', 'issuing_org': '', 'date': ''})
        if 'pdf_link' in st.session_state:
            del st.session_state['pdf_link']
        st.rerun()
        
    st.markdown("---")

    # --- Part 3: Final Generate Button and Download Link Display ---
    if st.button("Generate Resume PDF", type="primary", use_container_width=True):
        resume_data = {
            'full_name': st.session_state.get('full_name', ''),
            'job_title': st.session_state.get('job_title', ''),
            'email': st.session_state.get('email', ''),
            'phone': st.session_state.get('phone', ''),
            'linkedin': st.session_state.get('linkedin', ''),
            'summary': st.session_state.get('summary', ''),
            'work_experience': st.session_state.get('work_experience', []),
            'education': st.session_state.get('education', []),
            'projects': st.session_state.get('projects', []),
            'certifications': st.session_state.get('certifications', []),
            'skills': st.session_state.get('skills', '')
        }
        with st.spinner("Generating your professional resume..."):
            pdf_bytes = generate_pdf(resume_data)
            st.session_state.pdf_link = get_pdf_download_link(pdf_bytes)

    if 'pdf_link' in st.session_state:
        st.success("Your resume is ready!")
        st.markdown(st.session_state.pdf_link, unsafe_allow_html=True)