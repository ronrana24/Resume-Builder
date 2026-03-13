from datetime import date
from constants.constants import Degree, FieldOfStudy, Technology

class Link:
    def __init__(self, name, url):
        self.name = name
        self.url = url

class Person:
    def __init__(self, name: str, email: str, phone: str, links: list[Link]):
        self.name = name
        self.email = email
        self.phone = phone
        self.links = links

class Skill:
    def __init__(self, name: str, technology: list[str]):
        self.name = name
        self.technology = technology


class Experience:
    def __init__(self, company: str, position: str, description: list[str], start_date: date, end_date: date, location: str):
        self.company = company
        self.position = position
        self.description = description
        self.start_date = start_date
        self.end_date = end_date
        self.location = location

class Education:
    def __init__(self, school: str, degree: Degree, field_of_study: FieldOfStudy, start_year: int, end_year: int, gpa: float):
        self.school = school
        self.degree = degree
        self.field_of_study = field_of_study
        self.start_year = start_year
        self.end_year = end_year
        self.gpa = gpa

class PersonResumeData:
    def __init__(self, person: Person, skills: list[Skill], experiences: list[Experience], education: list[Education]):
        self.person = person
        self.skills = skills
        self.experiences = experiences
        self.education = education