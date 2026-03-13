from datetime import date
from data import Person, Link, Skill, Experience, Education, PersonResumeData
from constants.constants import Technology, Degree, FieldOfStudy


def generate_person_resume_data() -> PersonResumeData:
    person: Person = Person(
        name="Rahul Rana",
        email="rahul.rana2000.rr@gmail.com",
        phone="+91-7986950839",
        links=[
            Link(name="LinkedIn", url="https://www.linkedin.com/in/rahulrana24/"),
            Link(name="GitHub", url="https://github.com/ronrana24/"),
            Link(
                name="Portfolio", url="https://my-portfolio-omega-beryl-59.vercel.app/"
            ),
        ],
    )
    skills: list[Skill] = [
        Skill(
            name="Programming",
            technology=[
                Technology.PYTHON,
                Technology.JAVA,
                Technology.JAVASCRIPT,
                Technology.TYPESCRIPT,
                Technology.GOLANG,
            ],
        ),
        Skill(
            name="Frameworks & Libraries",
            technology=[
                Technology.REACT_JS,
                Technology.DJANGO,
                Technology.NODE_JS,
                Technology.EXPRESS_JS,
            ],
        ),
        Skill(
            name="Databases",
            technology=[
                Technology.POSTGRESQL,
                Technology.MYSQL,
                Technology.MONGODB,
                Technology.CLICK_HOUSE,
                Technology.REDIS,
            ],
        ),
        Skill(
            name="Cloud Technologies",
            technology=[
                Technology.AWS,
                Technology.DOCKER,
                Technology.GITHUB_ACTIONS,
                Technology.CI_CD,
            ],
        ),
        Skill(name="Messaging", technology=[Technology.KAFKA, Technology.RABBITMQ]),
        Skill(
            name="Testing & Tools",
            technology=[
                Technology.JEST,
                Technology.POSTMAN,
                Technology.SWAGGER,
                Technology.GIT,
                Technology.JIRA,
                Technology.VS_CODE,
                Technology.CURSOR,
            ],
        ),
    ]
    experiences: list[Experience] = [
        Experience(
            company="Spyne",
            position="Software Engineer",
            description=[
                "Spearheaded an automated alerting system in CUBE APM that tracked logic threshold violations and reduced developer response time by 30%, minimising system downtime.",
                "Engineered a fault-tolerant webhook system incorporating design patterns and message queuing to handle real-time event processing across multiple client integrations, reducing event failure rate by 35%.",
                "Pioneered a real-time streaming pipeline using Apache Kafka and MongoDB, enabling event-driven data distribution to downstream microservices and reducing data latency by 40%.",
                "Among a select group of developers chosen to architect a custom FTP system from scratch, enabling automated file transmission to remote servers and improving transfer efficiency by 40%.",
                "Supercharged MongoDB query performance through indexing and aggregation tuning, and introduced Redis caching to eliminate redundant database calls, improving overall application performance by 45%.",
                "Delivered a real-time ClickHouse dashboard to monitor application performance and client data ingestion, improving system observability and reducing manual reporting effort by 40%.",
                "Coordinated a team of 2+ developers, delegating tasks and providing technical mentorship that improved sprint velocity by 30%, conducting code reviews and knowledge-sharing sessions to ensure on-time delivery.",
                "Architected and integrated multiple client APIs and crafted scalable, robust RESTful APIs following best practices for performance, fault tolerance, and extensibility across microservices.",
            ],
            start_date=date(2024, 1, 1),
            end_date=date(2024, 12, 31),
            location="Gurgaon, India",
        ),
        Experience(
            company="Chimps",
            position="Software Engineer",
            description=[
                "Constructed a scalable, role-based document management microservice leveraging MVC architecture and open-source tooling (Paperless), enabling secure access for 100+ employees and improving operational efficiency and data security.",
                "Architected an AWS Lambda-powered serverless communication pipeline with SQS, integrating LeadSquared APIs with event-based asynchronous architectures to enhance customer engagement by 40%; streamlined deployment pipelines using Docker and GitHub Actions CI/CD.",
                "Revamped relational database schemas and fine-tuned PostgreSQL queries, slashing query execution time by 40%; introduced Redis caching to accelerate data retrieval for data-intensive applications.",
                "Built a multi-threaded data extraction pipeline for FMCSA, boosting processing efficiency by 33% and channelling results into a database for scalable analysis.",
                "Crafted and hardened robust RESTful APIs for seamless third-party service integration, ensuring high performance and scalability in a service-oriented architecture.",
                "Established a centralised logging system integrating Sentry for effective monitoring and observability, enabling streamlined issue tracking and faster resolution.",
                "Automated ETL processes via strategically deployed cron jobs, cutting manual effort by 20% and lifting data processing efficiency by 17%.",
            ],
            start_date=date(2024, 1, 1),
            end_date=date(2024, 12, 31),
            location="Hyderabad, India",
        ),
    ]
    education: list[Education] = [
        Education(
            school="Chitkara University",
            degree=Degree.BACHELOR.value,
            field_of_study=FieldOfStudy.COMPUTER_SCIENCE_AND_ENGINEERING.value,
            start_year=2020,
            end_year=2024,
            gpa=8.85,
        ),
    ]
    return PersonResumeData(person, skills, experiences, education)
