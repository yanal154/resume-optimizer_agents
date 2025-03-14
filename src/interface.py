
import streamlit as st
from crew import resume_crew  
from tools import extract_text_from_resume


st.title("📄 Resume Optimizer")

st.markdown("""
Upload your resume and enter the job description.
The app will optimize your resume to match the job requirements.
""")

uploaded_resume = st.file_uploader("Upload your Resume (PDF format)", type=['pdf'])

job_description = st.text_area("Enter the Job Description", height=250)

if st.button("Optimize Resume"):
    if uploaded_resume is not None and job_description:
        with open("temp_resume.pdf", "wb") as file:
            file.write(uploaded_resume.getbuffer())

        resume_text = extract_text_from_resume("temp_resume.pdf")

        with st.spinner('Optimizing your resume, please wait...'):
            optimized_result = resume_crew.kickoff(
                inputs={
                    "resume": resume_text,
                    "job_desc": job_description
                }
            )

        st.success("Resume optimization complete!")

        st.markdown("### 📝 Optimized Resume")
        st.text_area("Resume Optimizer", optimized_result, height=400)

    else:
        st.error("Please upload a resume and provide a job description.")