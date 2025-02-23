from grader import *

# defining main function
def main():
    rubric = {
        "Excellent (100)": "Menunjukkan pemahaman mendalam tentang topik dan memberikan analisis yang mendalam serta wawasan yang berharga.",
        "Good (80)": "Menunjukkan pemahaman yang baik tentang topik dan memberikan analisis yang relevan.",
        "Fair (60)": "Menunjukkan pemahaman dasar, tetapi analisisnya kurang mendalam.",
        "Poor (40)": "Menunjukkan pemahaman yang terbatas dan memberikan analisis yang dangkal.",
        "Very Poor (20)": "Menunjukkan kurangnya pemahaman tentang topik."
    }
    question = "Apakah Bezold Effect lebih berpengaruh pada jenis grafik tertentu, seperti diagram batang, scatter plot, atau peta choropleth? Mengapa?"
    answer = "Ya, Bezold Effect lebih berpengaruh pada peta choropleth dibandingkan diagram batang atau scatter plot. Soalnya, peta choropleth sangat bergantung pada gradasi warna untuk menunjukkan perbedaan data antar wilayah. Kalau ada perubahan warna karena efek Bezold, bisa bikin perbedaan antar daerah terlihat lebih jelas atau malah jadi samar. Sementara itu, di diagram batang dan scatter plot, warna biasanya dipakai untuk kategori yang terpisah, jadi efek ini nggak terlalu mengganggu interpretasi datanya."

    grade, feedback, response = grade_answer(answer, rubric, question)

    print(f"Nilai: {grade}")
    print(f"Umpan Balik: {feedback}")

    # print("\nRaw Gemini Response (for debugging):")  # Uncomment for debugging
    # print(response)

# Using the special variable 
# __name__
if __name__=="__main__":
    main()