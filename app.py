import streamlit as st

from modules.extractor import extract_actors

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

    else:
        st.warning("Belum ada aktor terdeteksi.")
