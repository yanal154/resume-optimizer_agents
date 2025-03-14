from crewai import Agent, Crew, Process, Task, LLM
import os
from tools import extract_text_from_resume





os.getenv("OPENAI_API_KEY")
base_llm = LLM(model="gpt-4o", temperature=0)


resume_parser_agent = Agent(
    role="Resume Content Analyzer",
    goal=(
        "Extract, classify, and structure all essential resume details "
        "with high accuracy. This includes personal information, professional summary, "
        "work experience, education, skills, certifications, achievements, and additional details."
    ),
    backstory=(
        "An experienced HR assistant and resume analysis expert who leverages advanced "
        "language models to quickly and reliably summarize resume content into a standardized, structured format."
    ),
    llm=base_llm
)

parse_resume_task = Task(
    description=(
        "Given the input resume text: {resume}, perform a comprehensive analysis to extract and organize the following sections:\n"
        "1. Personal Information (e.g., full name, contact details, address).\n"
        "2. Professional Summary or Objective Statement.\n"
        "3. Work Experience (including company names, job titles, employment dates, key responsibilities, and achievements).\n"
        "4. Educational Background (institutions, degrees, graduation dates).\n"
        "5. Skills and Competencies (technical skills, soft skills, language proficiencies).\n"
        "6. Certifications and Professional Training.\n"
        "7. Achievements, Awards, and Recognitions.\n"
        "8. Additional Information (e.g., volunteer work, languages, hobbies).\n\n"
        "Ensure the extracted data is formatted in a well-organized and structured manner, "
        "suitable for further HR processing and candidate evaluation."
    ),
    agent=resume_parser_agent,
    expected_output=(
        "A detailed and structured text summarizing the resume, with clearly defined sections for "
        "personal information, professional summary, work experience, education, skills, certifications, "
        "achievements, and additional information."
    )
)

job_desc_parser_agent = Agent(
    role="Job Description Content Analyzer",
    goal=(
        "Extract, classify, and structure all essential details from a job description. "
        "This includes key responsibilities, required skills, qualifications, work environment, benefits, "
        "and any additional relevant information."
    ),
    backstory=(
        "A seasoned recruitment consultant with extensive expertise in analyzing job listings. "
        "Skilled in identifying critical requirements and details to provide a comprehensive overview of the job role."
    ),
    llm=base_llm
)

parse_job_task = Task(
    description=(
        "Given the job description text: {job_desc}, perform an in-depth analysis to extract and organize the following sections:\n"
        "1. Job Responsibilities: Primary duties, tasks, and role expectations.\n"
        "2. Required Skills and Qualifications: Technical and soft skills, certifications, and educational requirements.\n"
        "3. Additional Details: Job benefits, work environment, and other critical notes.\n\n"
        "Ensure that the extracted information is clearly structured and formatted, "
        "making it suitable for further HR analysis and candidate matching."
    ),
    agent=job_desc_parser_agent,
    expected_output=(
        "A detailed and structured summary or data representation that captures the job description's key responsibilities, "
        "required skills, qualifications, and any additional relevant details."
    )
)

resume_validator_agent = Agent(
    role="Resume-Job Match Validator",
    goal=(
        "Evaluate the relevance of a candidate's existing resume to the provided job description, "
        "and determine if there is sufficient overlap in skills, experiences, and qualifications."
    ),
    backstory=(
        "An experienced HR analyst specialized in quickly assessing the suitability of resumes for specific job roles, "
        "ensuring candidates only pursue roles that align realistically with their backgrounds."
    ),
    llm=base_llm
)

validate_resume_task = Task(
    description=(
        "Given the structured resume information and structured job description summary, carefully evaluate "
        "the degree of alignment between the candidate's existing experience and the requirements of the job. "
        "If the candidate's experience, education, and skills align significantly with the job requirements, clearly state 'MATCH'. "
        "If the candidate's background does not reasonably match or is irrelevant to the job requirements, clearly state 'NO MATCH' with justification."
    ),
    agent=resume_validator_agent,
    context=[parse_resume_task, parse_job_task],
    expected_output=(
        "'MATCH' if the resume aligns well with the job requirements, or 'NO MATCH' with a brief justification if it does not."
    )
)


resume_improver_agent = Agent(
    role="Resume Improver",
    goal="Rewrite the resume to better match the job description, while preserving correctness",
    backstory="A professional resume writer with ATS knowledge, focusing on aligning user resumes with job requirements.",
    llm=base_llm
)

improve_resume_task = Task(
    description=(
        "If the validation result is 'MATCH', then combine the structured resume information with the structured job description summary "
        "to rewrite the user's resume, highlighting the most relevant experiences, skills, and achievements for this specific job. "
        "Preserve factual accuracy and avoid exaggeration. "
        "If the validation result is 'NO MATCH', clearly state that the resume cannot be improved for this role due to insufficient alignment with job requirements, "
        "and briefly summarize why."
    ),
    agent=resume_improver_agent,
    context=[parse_resume_task, parse_job_task, validate_resume_task],
    expected_output=(
        "An improved resume text tailored to the job description if validation was successful, "
        "or a clear explanation stating the resume is not suitable for the position."
    )
)







resume_crew = Crew(
    agents=[
        resume_parser_agent,
        job_desc_parser_agent,
        resume_validator_agent,  
        resume_improver_agent
    ],
    tasks=[
        parse_resume_task,
        parse_job_task,
        validate_resume_task,   
        improve_resume_task
    ],
    process=Process.sequential,
    verbose=True
)

