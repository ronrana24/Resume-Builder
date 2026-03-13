# Resume Builder

A simple Python + Jinja2 resume generator that builds a professional, single-page HTML resume from structured data.

## Features

- Generates `resume.html` from Python data models
- Uses Jinja2 template rendering
- Clean, print-friendly styling (A4 optimized)
- Easy to customize personal details, skills, experience, and education

## Tech Stack

- Python 3.10+
- Jinja2

## Project Structure

```text
.
|-- main.py
|-- utils.py
|-- data.py
|-- requirements.txt
`-- constants/
    |-- constants.py
    `-- template.html
```

- `main.py`: Entry point. Renders template and writes `resume.html`
- `utils.py`: Builds `PersonResumeData` with your resume content
- `data.py`: Data classes (`Person`, `Skill`, `Experience`, `Education`, etc.)
- `constants/constants.py`: Enum constants (technologies, degree, field of study)
- `constants/template.html`: Jinja2 HTML template + CSS styles

## Setup

1. Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Generate the resume:

```bash
python main.py
```

Output:

- `resume.html` in the project root

## Customize Resume Content

Edit `utils.py` inside `generate_person_resume_data()`:

- `person`: Name, email, phone, links
- `skills`: Each skill has:
  - `name` (section/key)
  - `technology` (array/list of technologies)
- `experiences`: Company, role, bullet points, dates, location
- `education`: Degree, field, school, years, CGPA

## Template Variables (Jinja2)

`main.py` passes these to `constants/template.html`:

- `person_name`
- `person_email`
- `person_phone`
- `personal_links`
- `skills`
- `experiences`
- `education`

## Print / Export to PDF (Single Page)

1. Open `resume.html` in your browser
2. Press print (`Cmd+P` on macOS)
3. Set:
   - Paper size: `A4`
   - Margins: `Default` or `None` (if content still fits)
   - Scale: `100%` (or slightly lower if needed)
4. Save as PDF

The template already includes print-oriented CSS to keep layout compact and professional.

## Common Troubleshooting

- **Module not found (`jinja2`)**
  - Activate `.venv` and reinstall requirements
- **Data not appearing in HTML**
  - Ensure keys passed in `main.py` match variable names in `template.html`
- **Resume spills onto second page**
  - Reduce content length slightly or lower print scale to 95-98%
