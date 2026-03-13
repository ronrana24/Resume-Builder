from data import PersonResumeData
from utils import generate_person_resume_data
from jinja2 import Template

def generate_html(person_resume_data: PersonResumeData):
    template = Template(open("constants/template.html").read())
    return template.render(person_name=person_resume_data.person.name,
        person_email=person_resume_data.person.email,
        person_phone=person_resume_data.person.phone,
        personal_links=person_resume_data.person.links,
        skills=person_resume_data.skills,
        experiences=person_resume_data.experiences,
        education=person_resume_data.education,
    )

if __name__ == "__main__":
    person_resume_data = generate_person_resume_data()
    html = generate_html(person_resume_data)
    output_file = "resume.html"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"✅  Resume generated → {output_file}")