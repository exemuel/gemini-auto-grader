import yaml
import pandas as pd
from grader import *

# defining main function
def main():
    # read the rubric file
    try:
        with open("rubric.yaml", "r") as stream:
            rubric = yaml.safe_load(stream)
    except FileNotFoundError:
        print("Error: rubric.yaml file not found.")
        return
    except yaml.YAMLError as e:
        print(f"Error parsing YAML: {e}")
        return
    
    # read the qa file
    try:
        # Read the QA file
        df_qas = pd.read_excel("qa-list.xlsx")
    except FileNotFoundError:
        print("Error: qa-list.xlsx file not found.")
        return
    except ValueError as e:
        print(f"Error reading qa-list.xlsx: {e}")
        return
    except Exception as e:
        print(f"Unexpected error while reading qa-list.xlsx: {e}")
        return

    list_grade = []
    list_feedback = []
    for row in df_qas.itertuples():
        grade, feedback, response = grade_answer(row.answer,
                                                 rubric,
                                                 row.question)
        list_grade.append(grade)
        list_feedback.append(feedback)

        # Pretty-print each grade-feedback pair
        print("=" * 40)
        print(f"Question: {row.question}")
        print(f"Answer: {row.answer}")
        print(f"Grade: {grade}")
        print(f"Feedback: {feedback}")
        print("=" * 40)

        # print("\nRaw Gemini Response (for debugging):")  # Uncomment for debugging
        # print(response)

    # append grades and feedback to DataFrame
    df_qas["grade"] = list_grade
    df_qas["feedback"] = list_feedback
    
    # save updated DataFrame
    try:
        df_qas.to_excel("grades.xlsx", index=False)
    except Exception as e:
        print(f"Error saving grades.xlsx: {e}")
        return

# Using the special variable 
# __name__
if __name__=="__main__":
    main()