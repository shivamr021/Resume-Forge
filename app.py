# file: app.py

import streamlit as st
import plotly.graph_objects as go
from streamlit_option_menu import option_menu

# Import your custom modules
from builder.form_handler import handle_resume_form
from reviewer.resume_parser import extract_text_from_pdf
from reviewer.ats_scoring import calculate_ats_score
from reviewer.ai_suggestions import get_ai_suggestions

# --- Core Layout and Page Configuration ---
st.set_page_config(
    page_title="AI Resume 360°",
    page_icon="📄",
    layout="wide"
)

# --- Externalized CSS ---
def load_custom_css():
    """Reads style.css and injects it into the app."""
    try:
        with open('assets\style.css') as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    except FileNotFoundError:
        st.warning("style.css not found. The app will use default styling.")

load_custom_css()

# --- Session State Initialization ---
if 'resume_text' not in st.session_state:
    st.session_state.resume_text = None
if 'job_description' not in st.session_state:
    st.session_state.job_description = ""
if 'analysis_done' not in st.session_state:
    st.session_state.analysis_done = False
if 'analysis_results' not in st.session_state:
    st.session_state.analysis_results = {}

# --- Main App Structure ---
st.title("AI Resume 360°")
st.markdown("Build, review, and get AI-powered suggestions to improve your resume.")
st.write("") # Spacer

# --- Top Navigation Bar ---
selected = option_menu(
    menu_title=None,
    options=["Build Resume", "ATS Review", "Suggestions"],
    icons=['pencil-square', 'graph-up-arrow', 'lightbulb'],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
)

# --- Section 1: Resume Builder ---
if selected == "Build Resume":
    st.header("📝 Resume Builder")
    st.write("Fill out your details below. You can add and remove sections for work and education dynamically.")
    st.markdown("---")
    handle_resume_form()

# --- Section 2: ATS Review ---
# In app.py, replace the entire "ATS Review" section with this

# --- NEW: Import the new function ---
from reviewer.ai_suggestions import get_general_ai_feedback

# --- Section 2: ATS Review (UPDATED) ---
if selected == "ATS Review":
    st.header("📊 ATS & Quality Review")
    st.write("Upload your resume for an analysis. You can either check it against a specific job or get a general quality score.")

    uploaded_resume = st.file_uploader("📄 Upload Your Resume (PDF)", type=["pdf"])

    # --- NEW: Checkbox to toggle review mode ---
    review_mode = st.checkbox("Review against a specific job description", value=True)

    if review_mode:
        st.session_state.job_description = st.text_area(
            "📝 Paste the Job Description Here",
            value=st.session_state.job_description,
            height=200
        )

    if st.button("🔍 Analyze Resume", use_container_width=True):
        if uploaded_resume:
            with st.spinner('AI is analyzing your resume... This may take a moment. ⏳'):
                st.session_state.resume_text = extract_text_from_pdf(uploaded_resume)
                
                # --- NEW: Logic to call the correct function ---
                if review_mode:
                    if st.session_state.job_description:
                        # Call the ATS scorer for specific job review
                        st.session_state.analysis_results = calculate_ats_score(st.session_state.resume_text, st.session_state.job_description)
                        st.session_state.analysis_done = True
                    else:
                        st.warning("⚠️ Please paste a job description for an ATS review.")
                        st.session_state.analysis_done = False
                else:
                    # Call the new general feedback function
                    st.session_state.analysis_results = get_general_ai_feedback(st.session_state.resume_text)
                    st.session_state.analysis_done = True

                if st.session_state.analysis_done:
                    st.toast('Analysis complete! 🎉', icon='✅')
        else:
            st.warning("⚠️ Please upload a resume to begin analysis.")

    # Display results if analysis has been run
    if st.session_state.analysis_done:
        results = st.session_state.analysis_results
        score_value = results.get('score', 0)
        feedback_text = results.get('feedback', '')
        
        st.markdown("---")
        # --- NEW: Dynamic subheader ---
        subheader_text = "🎯 ATS Match Score" if review_mode else "📈 Resume Quality Score"
        st.subheader(subheader_text)
        
        # (Your existing Plotly gauge chart code is perfect here)
        fig = go.Figure(go.Indicator(
            mode = "gauge+number",
            value = score_value,
            # ... rest of your fig code ...
        ))
        fig.update_layout(paper_bgcolor = "rgba(0,0,0,0)", font = {'color': "#FAFAFA", 'family': "Poppins"}, height=300)
        st.plotly_chart(fig, use_container_width=True)
        
        # --- NEW: Display feedback based on review mode ---
        if review_mode:
            st.info(feedback_text)
            st.markdown("### Skill Analysis")
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("✅ **Skills Matched**")
                for skill in results.get('matched_skills', []):
                    st.markdown(f"- {skill}")
            with col2:
                st.markdown("❌ **Skills to Add**")
                for skill in results.get('missing_skills', []):
                    st.markdown(f"- {skill}")
        else:
            # Display general feedback in a styled container
            with st.container(border=True):
                st.markdown(feedback_text)

                
# --- Section 3: Suggestions ---
if selected == "Suggestions":
    st.header("🧠 AI-Powered Improvement Suggestions")
    st.write("Get actionable feedback from our AI career coach to improve your resume.")

    if not st.session_state.analysis_done:
        st.info("💡 Please upload and analyze a resume in the 'ATS Review' section first.")
    else:
        # This is where the API call happens!
        with st.spinner('AI Coach is reviewing your resume...'):
            missing_skills = st.session_state.analysis_results.get('missing_skills', [])
            suggestions = get_ai_suggestions(
                st.session_state.resume_text, 
                st.session_state.job_description,
                missing_skills
            )
            st.markdown(suggestions)