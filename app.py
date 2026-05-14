import streamlit as st

from modules.extractor import extract_actors
from modules.matrix_builder import create_empty_matrix
from modules.relational_scoring import detect_relation_score

st.set_page_config(
    page_title="MatrixPIOM AI",
    layout="wide"
)

st.title("🧠 MatrixPIOM AI")
st.subheader("AI-assisted Institutional Matrix Analysis")

text = st.text_area(
    "Narasi Struktur Masalah",
    height=250
)

if st.button("🔄 Konversi ke Matriks"):

    actors = extract_actors(text)

    st.subheader("Aktor Terdeteksi")

    if actors:

        for actor in actors:
            st.write(f"• {actor}")

        matrix = create_empty_matrix(actors)

        score, keywords = detect_relation_score(text)

        for i in actors:
            for j in actors:

                if i != j:
                    matrix.loc[i, j] = score

        st.subheader("Problem Structuring Matrix")

        st.dataframe(
            matrix,
            use_container_width=True
        )

        st.subheader("Relational Interpretation")

        st.write(f"Detected keywords: {keywords}")

        st.write(f"Generated relational score: {score}")

    else:
        st.warning("Belum ada aktor terdeteksi.")
