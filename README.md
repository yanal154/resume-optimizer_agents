# Resume Optimizer 📝

This project is an AI-powered Resume Optimization System built using CrewAI. It analyzes resumes, extracts key information, matches them with job descriptions, and suggests improvements to make resumes more relevant to job postings.

## 🚀 Features

- Parses resume text and extracts structured information.
- Analyzes job descriptions to identify key requirements.
- Validates the relevance of a resume to a specific job.
- Generates an optimized resume that aligns with the job requirements.
- Uses GPT-4o for accurate AI-powered resume enhancement.

## 🏷️ How It Works

1. **Upload Resume** – Users upload their resume in PDF format.
2. **Enter Job Description** – Users provide the job description they want to optimize for.
3. **AI Analysis** – The system extracts information from both the resume and job description.
4. **Resume Validation** – It determines if the resume matches the job.
5. **Resume Optimization** – If the match is valid, it rewrites the resume to highlight relevant experience.

##  Installation

### Prerequisites
- Python 3.11+
- `pip` (Python package manager)
- OpenAI API Key

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/yanal154/resume-optimizer_agents
   cd resume-optimizer_agents
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate    # On Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Add your OpenAI API Key to a `.env` file:
   ```env
   OPENAI_API_KEY="your_api_key"
   ```

5. Run the Streamlit interface:
   ```bash
   streamlit run src/interface.py
   ```

## ⚙️ Technologies Used

- **Python** 🐍
- **CrewAI** 🤖
- **OpenAI GPT-4o** 🧪
- **Streamlit** 🎨
- **Fitz (PyMuPDF)** 🌟
- **python-docx** 📚

