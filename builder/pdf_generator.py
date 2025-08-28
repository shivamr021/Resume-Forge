# file: builder/pdf_generator.py

from fpdf import FPDF 
import os


_PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
_FONT_PATH = os.path.join(_PROJECT_ROOT, 'assets', 'fonts', 'DejaVuSans.ttf')
_FONT_PATH_BOLD = os.path.join(_PROJECT_ROOT, 'assets', 'fonts', 'DejaVuSans-Bold.ttf')

class ResumePDF(FPDF):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        try:
            self.add_font('DejaVu', '', _FONT_PATH, uni=True)
            self.add_font('DejaVu', 'B', _FONT_PATH_BOLD, uni=True)
            self.font_family = 'DejaVu'
        except RuntimeError as e:
            print(f"Font loading error: {e}. Falling back to Arial.")
            self.font_family = 'Arial'

        self.left_col_width = 65
        self.right_col_x = self.left_col_width + 5
        self.line_height = 5
        self.set_auto_page_break(auto=True, margin=15)

    def draw_background(self):
        self.set_fill_color(44, 62, 80)
        self.rect(0, 0, self.left_col_width, self.h, 'F')

    def add_main_header(self, name, title):
        self.set_xy(self.right_col_x, 15)
        self.set_font(self.font_family, 'B', 28)
        self.set_text_color(44, 62, 80)
        self.cell(0, 12, name, ln=True)
        self.set_x(self.right_col_x)
        self.set_font(self.font_family, '', 12)
        self.set_text_color(52, 73, 94)
        self.cell(0, 8, title, ln=True)

    def add_left_column_section(self, title, items, icon):
        self.set_xy(10, self.get_y() + 10)
        self.set_font(self.font_family, 'B', 12)
        self.set_text_color(255, 255, 255)
        self.cell(self.left_col_width - 20, 8, title, ln=True, border='B')
        self.ln(4)
        
        self.set_font(self.font_family, '', 9)
        for item in items:
            if item:
                self.set_x(10)
                # Use multi_cell to handle wrapping long lines (like emails)
                self.multi_cell(self.left_col_width - 20, self.line_height, f"{icon} {item.strip()}")
        self.ln(5)

    def add_right_column_section(self, title):
        # Adjust Y position to prevent overlap
        current_y = self.get_y()
        if current_y < 45: # Ensure we don't write over the header
            current_y = 45
        self.set_xy(self.right_col_x, current_y + 8)
        self.set_font(self.font_family, 'B', 14)
        self.set_text_color(44, 62, 80)
        self.cell(0, 8, title, ln=True, border='B')
        self.ln(4)

    def add_experience_entry(self, job_title, company, duration, description):
        self.set_x(self.right_col_x)
        self.set_font(self.font_family, 'B', 11)
        self.set_text_color(52, 73, 94)
        self.multi_cell(0, self.line_height, f"{job_title} at {company}")
        
        self.set_x(self.right_col_x)
        self.set_font(self.font_family, '', 9)
        self.set_text_color(127, 140, 141)
        self.cell(0, self.line_height, duration, ln=True)
        
        self.set_x(self.right_col_x)
        self.set_font(self.font_family, '', 10)
        self.set_text_color(52, 73, 94)
        # Prepend description points with a bullet point for clarity
        description_points = [f"• {line.strip()}" for line in description.split('\n') if line.strip()]
        self.multi_cell(0, self.line_height, "\n".join(description_points))
        self.ln(3)

    def add_simple_entry(self, title, subtitle):
        self.set_x(self.right_col_x)
        self.set_font(self.font_family, 'B', 11)
        self.set_text_color(52, 73, 94)
        self.cell(0, self.line_height, title, ln=True)
        
        self.set_x(self.right_col_x)
        self.set_font(self.font_family, '', 9)
        self.set_text_color(127, 140, 141)
        self.cell(0, self.line_height, subtitle, ln=True)
        self.ln(3)

def generate_pdf(data):
    """Generates a styled, two-column PDF from the provided form data."""
    pdf = ResumePDF('P', 'mm', 'A4')
    pdf.add_page()
    pdf.draw_background()

    # --- Left Column ---
    pdf.set_y(20)
    contact_items = [data.get('phone'), data.get('email'), data.get('linkedin')]
    pdf.add_left_column_section("CONTACT", contact_items, "•")
    
    if data.get('skills'):
        pdf.add_left_column_section("SKILLS", data.get('skills').split(','), "✓")

    if data.get('certifications'):
        cert_items = [f"{cert.get('cert_name', '')} - {cert.get('issuing_org', '')}" for cert in data.get('certifications', []) if cert.get('cert_name')]
        pdf.add_left_column_section("CERTIFICATIONS", cert_items, "🏆")

    # --- Right Column ---
    pdf.add_main_header(data.get('full_name', 'Your Name'), data.get('job_title', ''))

    if data.get('summary'):
        pdf.add_right_column_section("PROFESSIONAL SUMMARY")
        pdf.set_x(pdf.right_col_x)
        pdf.set_font(pdf.font_family, '', 10)
        pdf.set_text_color(52, 73, 94)
        pdf.multi_cell(0, pdf.line_height, data.get('summary'))

    if data.get('work_experience'):
        pdf.add_right_column_section("EXPERIENCE")
        for job in data.get('work_experience', []):
            if job.get('job_title'):
                pdf.add_experience_entry(job.get('job_title'), job.get('company'), job.get('duration'), job.get('description'))

    if data.get('projects'):
        pdf.add_right_column_section("PROJECTS")
        for proj in data.get('projects', []):
            if proj.get('project_name'):
                pdf.add_experience_entry(proj.get('project_name'), proj.get('link'), "", proj.get('description'))

    if data.get('education'):
        pdf.add_right_column_section("EDUCATION")
        for edu in data.get('education', []):
            if edu.get('degree'):
                pdf.add_simple_entry(edu.get('degree'), f"{edu.get('institution')} - {edu.get('year')}")

    # --- THE FIX ---
    # With fpdf2, output() with no destination returns a byte string by default.
    # No manual .encode() call is needed. This is much cleaner and more robust.
    return pdf.output()