import streamlit as st

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
    st.success("Engine siap dikembangkan 😄")
