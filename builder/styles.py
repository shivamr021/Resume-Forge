import streamlit as st
def load_css():
    """Load custom CSS styles for better UI appearance"""
    st.markdown("""
    <style>
    /* Main container styling */
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    
    /* Section headers */
    .stSubheader {
        color: #1f77b4;
        font-weight: 600;
        margin-bottom: 1rem;
        padding-bottom: 0.5rem;
        border-bottom: 2px solid #e0e0e0;
    }
    
    /* Form inputs */
    .stTextInput > div > div > input {
        border-radius: 8px;
        border: 1px solid #e0e0e0;
    }
    
    .stTextArea > div > div > textarea {
        border-radius: 8px;
        border: 1px solid #e0e0e0;
    }
    
    /* Buttons */
    .stButton > button {
        border-radius: 8px;
        border: none;
        background-color: #1f77b4;
        color: white;
        font-weight: 500;
        padding: 0.5rem 1rem;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        background-color: #1565c0;
        transform: translateY(-1px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
    
    /* Remove button styling */
    button[data-testid="baseButton-secondary"] {
        background-color: #dc3545 !important;
        color: white !important;
        border: none !important;
        border-radius: 50% !important;
        width: 40px !important;
        height: 40px !important;
        padding: 0 !important;
        font-size: 16px !important;
    }
    
    button[data-testid="baseButton-secondary"]:hover {
        background-color: #c82333 !important;
    }
    
    /* Add button styling */
    button[key="add_education"] {
        background-color: #28a745 !important;
        color: white !important;
        border: none !important;
        border-radius: 8px !important;
        padding: 0.5rem 1rem !important;
        font-weight: 500 !important;
    }
    
    button[key="add_education"]:hover {
        background-color: #218838 !important;
    }
    
    /* Submit button */
    .stFormSubmitButton > button {
        background-color: #28a745 !important;
        color: white !important;
        border: none !important;
        border-radius: 8px !important;
        padding: 0.75rem 2rem !important;
        font-weight: 600 !important;
        font-size: 1.1rem !important;
        width: 100% !important;
        margin-top: 1rem !important;
    }
    
    .stFormSubmitButton > button:hover {
        background-color: #218838 !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 12px rgba(0,0,0,0.15) !important;
    }
    
    /* Education entry containers */
    .stMarkdown {
        margin-bottom: 0.5rem;
    }
    
    /* Horizontal line styling */
    hr {
        margin: 1.5rem 0;
        border: none;
        border-top: 1px solid #e0e0e0;
    }
    
    /* Placeholder text styling */
    ::placeholder {
        color: #999 !important;
        opacity: 1;
    }
    
    /* Focus states */
    .stTextInput > div > div > input:focus,
    .stTextArea > div > div > textarea:focus {
        border-color: #1f77b4 !important;
        box-shadow: 0 0 0 2px rgba(31, 119, 180, 0.2) !important;
    }
    </style>
    """, unsafe_allow_html=True) 