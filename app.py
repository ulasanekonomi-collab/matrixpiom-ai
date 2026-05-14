import streamlit as st

from modules.extractor import extract_actors
from modules.matrix_builder import create_empty_matrix
from modules.relational_scoring import detect_pairwise_relations

st.set_page_config(
    page_title="MatrixPIOM AI",
    layout="wide"
)

st.title("🧠 MatrixPIOM AI")
st.subheader("AI-assisted Institutional Matrix Analysis")
with st.expander("📝 Panduan Penulisan Narasi"):

    st.markdown("""
    Tuliskan narasi masalah secara jelas dan terstruktur.

    Narasi sebaiknya memuat:

    - siapa aktor yang terlibat,
    - hubungan antaraktor,
    - dukungan atau konflik,
    - pihak yang mempengaruhi,
    - serta dampak yang terjadi.

    Contoh:

    Pemerintah Daerah bekerja sama dengan Investor Tambang,
    tetapi Masyarakat Adat menolak proyek tersebut karena
    dampak lingkungan.
    """)
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

        relations = detect_pairwise_relations(
            text,
            actors
        )

        for relation in relations:

            source = relation["source"]
            target = relation["target"]
            score = relation["score"]

            matrix.loc[source, target] = score

        st.subheader("Problem Structuring Matrix")

        styled_matrix = matrix.style.background_gradient(
            cmap="RdYlGn",
            axis=None
        )

        st.dataframe(
            styled_matrix,
            use_container_width=True
        )

        st.subheader("Relational Interpretation")

        st.subheader("Detected Relations")

        for relation in relations:

            st.write(
                f"{relation['source']} → "
                f"{relation['target']} | "
                f"{relation['keyword']} | "
                f"score = {relation['score']}"
                )
    else:
        st.warning("Belum ada aktor terdeteksi.")
