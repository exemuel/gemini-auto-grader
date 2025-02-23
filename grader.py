import os
from dotenv import load_dotenv  # Import dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate

# Load environment variables from .env file
load_dotenv()

# Get the API key from the environment variables
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    raise ValueError("GOOGLE_API_KEY environment variable not set. Create a .env file.")

def grade_answer(answer, rubric, question):
    """Grades an answer using LangChain's ChatGoogleGenerativeAI and ChatPromptTemplate."""

    llm = ChatGoogleGenerativeAI(model="gemini-2.0-pro-exp-02-05", temperature=0.2, api_key=api_key)

    prompt = ChatPromptTemplate.from_messages([
        ("system", "Anda adalah asisten AI yang menilai jawaban siswa berdasarkan rubrik dan memberikan umpan balik."),
        ("user", f"""
        ## Pertanyaan:
        {question}

        ## Jawaban:
        {answer}

        ## Rubrik:
        {format_rubric(rubric)}

        ## Penilaian dan Umpan Balik:
        Berdasarkan rubrik yang diberikan, tetapkan nilai untuk jawaban dan berikan umpan balik yang terperinci. Jelaskan pilihan nilai Anda dengan merujuk pada bagian-bagian tertentu dari jawaban dan bagaimana bagian-bagian tersebut sesuai (atau tidak sesuai) dengan kriteria rubrik. Bersikaplah konstruktif dan tawarkan saran untuk perbaikan. Format tanggapan sebagai berikut:

        **Nilai:** [Tingkatan Nilai] (e.g., Excellent (100), Good (80), Fair (60), Poor (40), Very Poor (20))
        **Umpan Balik:** [Umpan balik terperinci yang menjelaskan nilai dan saran untuk perbaikan]
        """)
    ])


    try:
        final_prompt = prompt.format() # No input variables in this case
        response = llm.invoke(final_prompt)  # Call Gemini through LangChain

        grade = extract_grade(response.content)  # Access content attribute
        feedback = extract_feedback(response.content)

        return grade, feedback, response.content # Return string content

    except Exception as e:
        return "Error", f"An error occurred: {e}", None


def format_rubric(rubric):
    """Formats the rubric for the prompt."""
    formatted_rubric = ""
    for level, description in rubric.items():
        formatted_rubric += f"- **{level}:** {description}\n"
    return formatted_rubric


def extract_grade(text):
    """Extracts the grade from the Gemini response."""
    try:
        lines = text.splitlines()
        for line in lines:
            if line.startswith("**Nilai:**"):
                return line.split("**Nilai:**")[1].strip()
        return "Nilai Tidak Ditemukan"
    except:
        return "Nilai Tidak Ditemukan"


def extract_feedback(text):
    """Extracts the feedback from the Gemini Response."""
    try:
        lines = text.splitlines()
        feedback_started = False
        feedback_lines = []
        for line in lines:
            if line.startswith("**Umpan Balik:**"):
                feedback_started = True
                continue  # don't include the "**Feedback:**" line itself
            if feedback_started:
                feedback_lines.append(line)
        return "\n".join(feedback_lines).strip()
    except:
        return "Umpan Balik Tidak Ditemukan"