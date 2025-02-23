# Gemini Auto Grader

This Python tool uses the Gemini API to automatically grade student answers based on a provided rubric and generates detailed feedback.

## Features

*   Automated grading of text-based answers.
*   Rubric-based assessment.
*   Detailed feedback generation, including justifications for the assigned grade and suggestions for improvement.
*   Uses the Gemini Pro model (or other suitable Gemini models).
*   Easy to use and integrate into existing workflows.

## Installation

1.  Clone the repository:
    ```bash
    git clone [https://github.com/YOUR_USERNAME/gemini-auto-grader.git](https://www.google.com/search?q=https://github.com/YOUR_USERNAME/gemini-auto-grader.git)  # Replace with your username
    ```

2.  Navigate to the directory:
    ```bash
    cd gemini-auto-grader
    ```

3.  Install the required libraries:
    ```bash
    pip install langchain_google_genai
    ```

4.  Set your Gemini API key as an environment variable named `GOOGLE_API_KEY`.  The recommended way to do this is to use a `.env` file in the same directory as your script:

    ```
    GOOGLE_API_KEY=YOUR_ACTUAL_API_KEY
    ```
    Then, install the `python-dotenv` package:
    ```bash
    pip install python-dotenv
    ```
    And import it in your Python file:
    ```python
    import os
    from dotenv import load_dotenv
    load_dotenv() # Load environment variables from .env file
    api_key = os.getenv("GOOGLE_API_KEY")
    ```

## Usage

```python
from gemini_grader import grade_answer, format_rubric, extract_grade, extract_feedback # Import from your script

# Define your rubric
rubric = {
    "Excellent": "Demonstrates a deep understanding of the topic and provides insightful analysis.",
    "Good": "Shows a good understanding of the topic and provides relevant analysis.",
    "Fair": "Demonstrates a basic understanding but lacks depth in analysis.",
    "Poor": "Shows a limited understanding and provides superficial analysis.",
    "Very Poor": "Demonstrates a lack of understanding of the topic."
}

# Example question and answer
question = "Explain the concept of Artificial Intelligence."
answer = "AI is like, computers that can think.  They can do stuff like play games and recognize faces.  It's pretty cool."

# Grade the answer and get feedback
grade, feedback, response = grade_answer(answer, rubric, question)

# Print the results
print(f"Grade: {grade}")
print(f"Feedback: {feedback}")

# (Optional) Print the raw Gemini response for debugging
# print("\nRaw Gemini Response (for debugging):")
# print(response.result)


## Contributing
Contributions are welcome! Please open an issue or submit a pull request.

## License
MIT License

## Contact
Samuel Situmeang (samsitumeang@gmail.com)
