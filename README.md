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
Check `main.py`

```python
from gemini_grader import grade_answer, format_rubric, extract_grade, extract_feedback # Import from your script

# Define your rubric
rubric = {
    "Excellent (100)": "Menunjukkan pemahaman mendalam tentang topik dan memberikan analisis yang mendalam serta wawasan yang berharga.",
    "Good (80)": "Menunjukkan pemahaman yang baik tentang topik dan memberikan analisis yang relevan.",
    "Fair (60)": "Menunjukkan pemahaman dasar, tetapi analisisnya kurang mendalam.",
    "Poor (40)": "Menunjukkan pemahaman yang terbatas dan memberikan analisis yang dangkal.",
    "Very Poor (20)": "Menunjukkan kurangnya pemahaman tentang topik."
}

# Example question and answer
question = "Apakah Bezold Effect lebih berpengaruh pada jenis grafik tertentu, seperti diagram batang, scatter plot, atau peta choropleth? Mengapa?"
answer = "Ya, Bezold Effect lebih berpengaruh pada peta choropleth dibandingkan diagram batang atau scatter plot. Soalnya, peta choropleth sangat bergantung pada gradasi warna untuk menunjukkan perbedaan data antar wilayah. Kalau ada perubahan warna karena efek Bezold, bisa bikin perbedaan antar daerah terlihat lebih jelas atau malah jadi samar. Sementara itu, di diagram batang dan scatter plot, warna biasanya dipakai untuk kategori yang terpisah, jadi efek ini nggak terlalu mengganggu interpretasi datanya."

# Grade the answer and get feedback
grade, feedback, response = grade_answer(answer, rubric, question)

# Print the results
print(f"Nilai: {grade}")
print(f"Umpan Balik: {feedback}")

# (Optional) Print the raw Gemini response for debugging
# print("\nRaw Gemini Response (for debugging):")
# print(response.result)


## Contributing
Contributions are welcome! Please open an issue or submit a pull request.

## License
MIT License

## Contact
Samuel Situmeang (samsitumeang@gmail.com)
