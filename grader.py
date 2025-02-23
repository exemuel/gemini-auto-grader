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
        ("system", "You are an AI assistant that grades student answers based on a rubric and provides feedback."),
        ("user", f"""
        ## Question:
        {question}

        ## Answer:
        {answer}

        ## Rubric:
        {format_rubric(rubric)}

        ## Grading and Feedback:
        Based on the provided rubric, assign a grade to the answer and provide detailed feedback. Justify your grade choice by referencing specific parts of the answer and how they align (or don't align) with the rubric criteria. Be constructive and offer suggestions for improvement. Format the response as follows:

        **Grade:** [Grade Level] (e.g., Excellent, Good, Fair, Poor, Very Poor)
        **Feedback:** [Detailed feedback explaining the grade and suggestions for improvement]
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
            if line.startswith("**Grade:**"):
                return line.split("**Grade:**")[1].strip()
        return "Grade Not Found"
    except:
        return "Grade Not Found"


def extract_feedback(text):
    """Extracts the feedback from the Gemini Response."""
    try:
        lines = text.splitlines()
        feedback_started = False
        feedback_lines = []
        for line in lines:
            if line.startswith("**Feedback:**"):
                feedback_started = True
                continue  # don't include the "**Feedback:**" line itself
            if feedback_started:
                feedback_lines.append(line)
        return "\n".join(feedback_lines).strip()
    except:
        return "Feedback Not Found"

# defining main function
def main():
    rubric = {
        "Excellent": "Demonstrates a deep understanding of the topic and provides insightful analysis.",
        "Good": "Shows a good understanding of the topic and provides relevant analysis.",
        "Fair": "Demonstrates a basic understanding but lacks depth in analysis.",
        "Poor": "Shows a limited understanding and provides superficial analysis.",
        "Very Poor": "Demonstrates a lack of understanding of the topic."
    }
    question = "Explain the concept of Artificial Intelligence."
    answer = "AI is like, computers that can think. They can do stuff like play games and recognize faces. It's pretty cool."

    grade, feedback, response = grade_answer(answer, rubric, question)

    print(f"Grade: {grade}")
    print(f"Feedback: {feedback}")

    # print("\nRaw Gemini Response (for debugging):")  # Uncomment for debugging
    # print(response)

# Using the special variable 
# __name__
if __name__=="__main__":
    main()