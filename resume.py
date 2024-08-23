import pandas as pd
import numpy as np
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle

# Function to generate resume
def generate_resume(data):
    pdf_file = 'resume.pdf'
    doc = SimpleDocTemplate(pdf_file, pagesize=letter)
    elements = []

    styles = getSampleStyleSheet()
    title_style = styles['Title']
    heading_style = styles['Heading1']
    normal_style = styles['Normal']

    # Title
    title = Paragraph(f"{data['name']}", title_style)
    elements.append(title)

    # Contact Information
    contact_info = Paragraph(f"Email: {data['email']}<br/>Phone: {data['phone']}", normal_style)
    elements.append(contact_info)
    elements.append(Paragraph("<br/>", normal_style))

    # Experience Section
    elements.append(Paragraph("<b>Experience</b>", heading_style))
    experience_data = [(job['position'], job['company'], job['duration'], job['details']) for job in data['experience']]
    table = Table([['Position', 'Company', 'Duration', 'Details']] + experience_data)
    table.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                               ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                               ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                               ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                               ('GRID', (0, 0), (-1, -1), 1, colors.black)]))
    elements.append(table)
    elements.append(Paragraph("<br/>", normal_style))

    # Education Section
    elements.append(Paragraph("<b>Education</b>", heading_style))
    education_data = [(edu['degree'], edu['institution'], edu['year']) for edu in data['education']]
    edu_table = Table([['Degree', 'Institution', 'Year']] + education_data)
    edu_table.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                                   ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                                   ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                                   ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                                   ('GRID', (0, 0), (-1, -1), 1, colors.black)]))
    elements.append(edu_table)
    elements.append(Paragraph("<br/>", normal_style))

    # Skills Section
    elements.append(Paragraph("<b>Skills</b>", heading_style))
    skills = Paragraph(f"{', '.join(data['skills'])}", normal_style)
    elements.append(skills)

    # Save the document
    doc.build(elements)
    print(f"Resume has been saved as {pdf_file}")

# Function to take user input
def get_user_input():
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    phone = input("Enter your phone number: ")

    experience = []
    num_experience = int(input("How many job experiences do you want to add? "))
    for _ in range(num_experience):
        position = input("Enter job position: ")
        company = input("Enter company name: ")
        duration = input("Enter job duration: ")
        details = input("Enter job details: ")
        experience.append({'position': position, 'company': company, 'duration': duration, 'details': details})

    education = []
    num_education = int(input("How many educational qualifications do you want to add? "))
    for _ in range(num_education):
        degree = input("Enter degree: ")
        institution = input("Enter institution: ")
        year = input("Enter graduation year: ")
        education.append({'degree': degree, 'institution': institution, 'year': year})

    skills = input("Enter your skills (separated by commas): ").split(',')

    return {
        'name': name,
        'email': email,
        'phone': phone,
        'experience': experience,
        'education': education,
        'skills': [skill.strip() for skill in skills]
    }

# Get data from user and generate resume
resume_data = get_user_input()
generate_resume(resume_data)
