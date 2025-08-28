# file: builder/pdf_generator.py

from fpdf import FPDF
import os

_PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
_FONT_PATH_REGULAR = os.path.abspath(os.path.join(_PROJECT_ROOT, 'assets', 'fonts', 'DejaVuSans.ttf'))
_FONT_PATH_BOLD = os.path.abspath(os.path.join(_PROJECT_ROOT, 'assets', 'fonts', 'DejaVuSans-Bold.ttf'))

class ResumePDF(FPDF):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        try:
            self.add_font('DejaVu', '', _FONT_PATH_REGULAR, uni=True)
            self.add_font('DejaVu', 'B', _FONT_PATH_BOLD, uni=True)
            self.font_family = 'DejaVu'
        except RuntimeError as e:
            print(f"Font loading error: {e}. Falling back to Arial.")
            self.font_family = 'Arial'

        self.left_col_width = 70
        self.right_col_x = self.left_col_width + 5
        self.line_height = 5
        self.set_auto_page_break(auto=True, margin=15)

    def draw_background(self):
        self.set_fill_color(44, 62, 80)
        self.rect(0, 0, self.left_col_width, self.h, 'F')

    def add_main_header(self, name, title):
        self.set_xy(self.right_col_x, 15)
        self.set_font(self.font_family, 'B', 26)
        self.set_text_color(44, 62, 80)
        self.cell(0, 9, name, ln=True)
        self.set_x(self.right_col_x)
        self.set_font(self.font_family, '', 11)
        self.set_text_color(52, 73, 94)
        self.cell(0, 6, title, ln=True)

    def add_left_column_section(self, title):
        self.set_xy(10, self.get_y() + 5)
        self.set_font(self.font_family, 'B', 12)
        self.set_text_color(255, 255, 255)
        self.cell(self.left_col_width - 20, 8, title, ln=True, border='B')
        self.ln(2)

    # --- NEW: Dedicated functions for different contact types ---
    def add_contact_item(self, icon, text):
        if not text: return
        self.set_x(10)
        self.set_font_size(9)
        self.multi_cell(self.left_col_width - 20, self.line_height, f"{icon} {text.strip()}")

    def add_contact_link(self, icon, full_url):
        if not full_url: return
        display_text = full_url.replace("https://www.", "").replace("http://www.", "").replace("https://", "")
        if display_text.endswith('/'): display_text = display_text[:-1]

        self.set_x(10)
        self.set_font_size(8)
        self.set_text_color(200, 220, 255)
        self.write(self.line_height, f"{icon} {display_text}", link=full_url)
        self.ln(self.line_height)
        self.set_text_color(255, 255, 255) # Reset color

    def add_right_column_section(self, title):
        current_y = self.get_y()
        if current_y < 40: current_y = 40
        self.set_xy(self.right_col_x, current_y + 4)
        self.set_font(self.font_family, 'B', 14)
        self.set_text_color(44, 62, 80)
        self.cell(0, 8, title, ln=True, border='B')
        self.ln(2)

    def add_experience_entry(self, title, subtitle, date, description, links=None):
        self.set_x(self.right_col_x)
        self.set_font(self.font_family, 'B', 11)
        self.set_text_color(52, 73, 94)
        self.multi_cell(0, self.line_height, title)
        
        if subtitle:
            y_before = self.get_y()
            self.set_x(self.right_col_x)
            self.set_font(self.font_family, '', 10)
            self.cell(0, self.line_height, subtitle)
            
            self.set_y(y_before)
            self.set_font(self.font_family, '', 9)
            self.set_text_color(127, 140, 141)
            date_width = self.get_string_width(date)
            x_pos = self.w - self.r_margin - date_width
            self.set_x(x_pos)
            self.cell(0, self.line_height, date, ln=True)
        
        if links and any(links):
            self.ln(-1) 
            self.set_x(self.right_col_x)
            self.set_font_size(8)
            self.set_text_color(82, 127, 141)
            link_text = " | ".join(filter(None, links))
            self.multi_cell(0, self.line_height - 1, link_text)
            self.set_font_size(10)
            self.ln(1)

        self.set_x(self.right_col_x)
        self.set_font(self.font_family, '', 10)
        self.set_text_color(52, 73, 94)
        description_points = [f"• {line.strip()}" for line in description.split('\n') if line.strip()]
        self.multi_cell(0, self.line_height, "\n".join(description_points))
        self.ln(2)

    def add_education_entry(self, degree, institution, year, cgpa):
        subtitle = institution
        if cgpa: subtitle += f" (CGPA: {cgpa})"

        y_before = self.get_y()
        self.set_x(self.right_col_x)
        self.set_font(self.font_family, 'B', 11)
        self.set_text_color(52, 73, 94)
        self.cell(0, self.line_height, degree)

        self.set_y(y_before)
        self.set_font(self.font_family, '', 9)
        self.set_text_color(127, 140, 141)
        year_width = self.get_string_width(year)
        x_pos = self.w - self.r_margin - year_width
        self.set_x(x_pos)
        self.cell(0, self.line_height, year, ln=True)

        self.set_x(self.right_col_x)
        self.set_font(self.font_family, '', 10)
        self.set_text_color(52, 73, 94)
        self.multi_cell(0, self.line_height, subtitle)
        self.ln(2)

# --- Main PDF Generation Function ---
def generate_pdf(data):
    pdf = ResumePDF('P', 'mm', 'A4')
    pdf.add_page()
    pdf.draw_background()

    # --- UPDATED: New logic for rendering the contact section reliably ---
    pdf.set_y(15)
    pdf.add_left_column_section("CONTACT")
    pdf.add_contact_item("•", data.get('phone'))
    pdf.add_contact_item("•", data.get('email'))
    pdf.add_contact_link("•", data.get('linkedin')) # Uses the new link handler
    pdf.ln(2) # Add some space after the contact section

    if data.get('skills'):
        pdf.add_left_column_section("SKILLS")
        pdf.set_font_size(9)
        for skill in data.get('skills').split(','):
            if skill.strip():
                pdf.set_x(10)
                pdf.multi_cell(pdf.left_col_width - 20, pdf.line_height, f"✓ {skill.strip()}")
        pdf.ln(1)

    if data.get('certifications'):
        pdf.add_left_column_section("CERTIFICATIONS")
        pdf.set_font_size(9)
        for cert in data.get('certifications', []):
            if cert.get('cert_name'):
                cert_text = f"{cert.get('cert_name', '')} - {cert.get('issuing_org', '')}"
                pdf.set_x(10)
                pdf.multi_cell(pdf.left_col_width - 20, pdf.line_height, f"★ {cert_text}")
        pdf.ln(1)

    # Right Column
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
                links = [proj.get('live_link'), proj.get('github_link')]
                pdf.add_experience_entry(proj.get('project_name'), "", "", proj.get('description'), links=links)

    if data.get('education'):
        pdf.add_right_column_section("EDUCATION")
        for edu in data.get('education', []):
            if edu.get('degree'):
                pdf.add_education_entry(edu.get('degree'), edu.get('institution'), edu.get('year'), edu.get('cgpa'))

    return pdf.output()