import yaml
from grader import *

# defining main function
def main():
    with open("rubric.yaml", "r") as stream:
        rubric = yaml.safe_load(stream)
    
    print(rubric)
    # question = "Apakah Bezold Effect lebih berpengaruh pada jenis grafik tertentu, seperti diagram batang, scatter plot, atau peta choropleth? Mengapa?"
    # answer = "Ya, Bezold Effect lebih berpengaruh pada peta choropleth dibandingkan diagram batang atau scatter plot. Soalnya, peta choropleth sangat bergantung pada gradasi warna untuk menunjukkan perbedaan data antar wilayah. Kalau ada perubahan warna karena efek Bezold, bisa bikin perbedaan antar daerah terlihat lebih jelas atau malah jadi samar. Sementara itu, di diagram batang dan scatter plot, warna biasanya dipakai untuk kategori yang terpisah, jadi efek ini nggak terlalu mengganggu interpretasi datanya."

    # grade, feedback, response = grade_answer(answer, rubric, question)

    # print(f"Nilai: {grade}")
    # print(f"Umpan Balik: {feedback}")

    # print("\nRaw Gemini Response (for debugging):")  # Uncomment for debugging
    # print(response)

# Using the special variable 
# __name__
if __name__=="__main__":
    main()