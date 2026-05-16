import streamlit as st

from modules.extractor import extract_actors
from modules.matrix_builder import create_empty_matrix

from modules.relational_scoring import (
    detect_pairwise_relations,
    detect_power_relations,
    detect_semantic_relations
)
from modules.semantic_parser import (
    extract_semantic_tags,
    extract_relation_tags
)

from modules.power_index import (
    compute_power_index
)
st.set_page_config(
    page_title="POWER & INSTITUTIONA OUTCOME MAPS",
    layout="wide"
)
st.sidebar.image(
    "assets/yuka.png",
    use_container_width=True
)

st.sidebar.markdown("""
### Dikembangkan oleh
**Yuhka Sundaya**  
Ekonomi Pembangunan  
Universitas Islam Bandung (UNISBA)
""")

st.title("POWER & INSTITUTIONAL OUTCOME MAP")
st.subheader("AI-assisted Institutional Matrix Analysis")
with st.expander("📝 Panduan Penulisan Narasi"):

    st.markdown("""
    Tuliskan narasi masalah kelembagaan secara jelas dan terstruktur.

    Narasi dapat ditulis dengan dua cara:

    1. Mode Narasi Natural
    
    Tuliskan narasi seperti penjelasan biasa.
    
    Contoh:
    
    Pemerintah Daerah bekerja sama dengan Investor Tambang dalam pengelolaan izin tambang. 
    Namun Masyarakat Adat menolak proyek tersebut karena dampak lingkungan. 
    LSM mempengaruhi opini masyarakat melalui kampanye publik. 
    Investor mendominasi pasar tambang di wilayah tersebut.

    2. Mode Semantic Tag (Opsional)
    
    Gunakan tag untuk membantu identifikasi aktor, arena, sumber daya, atau institusi secara lebih presisi.
    
    Tag yang tersedia:
    • (actor)
    • (arena)
    • (resource)
    • (institution)
    • (issue)

    Contoh:
    
    (actor) Pemerintah Daerah bekerja sama dengan (actor) Investor Tambang dalam pengelolaan (resource) izin tambang. 
    Namun (actor) Masyarakat Adat menolak proyek tersebut karena (issue) dampak lingkungan.

    Contoh Kata Relasi
    • Konflik:
    menolak, mengkritik, melawan
    • Kolaborasi:
    bekerja sama, mendukung
    • Pengaruh:
    mempengaruhi, mendorong
    • Kekuasaan:
    mengendalikan, mendominasi
    """)
text = st.text_area(
    "Narasi Struktur Masalah",
    height=250
)
semantic_tags = extract_semantic_tags(text)
relation_tags = extract_relation_tags(text)
semantic_relations = extract_relation_tags(text)
# tampil ontology dulu
if False:
    st.subheader("Semantic Ontology Detection")
    
    for category, values in semantic_tags.items():
        st.markdown(f"### {category.upper()}")
        st.write(values)

# baru proses matriks
if st.button("🔄 Konversi ke Matriks"):

    actors = extract_actors(text)

    st.subheader("Aktor Terdeteksi")

    if actors:

        for actor in actors:
            st.write(f"• {actor}")

        conflict_matrix = create_empty_matrix(actors)
        influence_matrix = create_empty_matrix(actors)
        collaboration_matrix = create_empty_matrix(actors)
        power_matrix = create_empty_matrix(actors)
        
        relations = detect_pairwise_relations(
            text,
            actors
        )

        power_relations = detect_power_relations(
            text,
            semantic_tags
        )
        semantic_relations = detect_semantic_relations(
            relation_tags
        )

        relations.extend(power_relations)
        relations.extend(semantic_relations)

        for relation in relations:

            source = relation["source"]
            target = relation["target"]
            score = relation["score"]

            relation_type = relation["relation_type"]

            if relation_type == "conflict":
                conflict_matrix.loc[source, target] = score

            elif relation_type == "influence":
                influence_matrix.loc[source, target] = score

            elif relation_type == "collaboration":
                collaboration_matrix.loc[source, target] = score

            elif relation_type == "power":
                target = relation["target"]
                power_matrix.loc[source, target] = score
                
        tab1, tab2, tab3, tab4 = st.tabs([
            "Conflict",
            "Influence",
            "Collaboration",
            "Power"
        ])

        with tab1:

            st.subheader("Conflict Matrix")

            styled_matrix = conflict_matrix.style.background_gradient(
                cmap="RdYlGn",
                vmin=-5,
                vmax=5,
                axis=None
            )

            st.dataframe(
                styled_matrix,
                use_container_width=True
            )

        with tab2:

            st.subheader("Influence Matrix")

            styled_matrix = influence_matrix.style.background_gradient(
                cmap="RdYlGn",
                vmin=-5,
                vmax=5,
                axis=None
            )

            st.dataframe(
                styled_matrix,
                use_container_width=True
            )

        with tab3:

             st.subheader("Collaboration Matrix")

             styled_matrix = collaboration_matrix.style.background_gradient(
                cmap="RdYlGn",
                vmin=-5,
                vmax=5,
                axis=None
             )

             st.dataframe(
                 styled_matrix,
                 use_container_width=True
             )

        with tab4:

            st.subheader("Power Matrix")

            styled_matrix = power_matrix.style.background_gradient(
                cmap="RdYlGn",
                vmin=-5,
                vmax=5,
                axis=None
            )

            st.dataframe(
                styled_matrix,
                use_container_width=True
            )
            power_index_df = compute_power_index(
                actors,
                influence_matrix,
                power_matrix,
                collaboration_matrix,
                conflict_matrix
            )
            st.subheader("Power Index Analysis")

            st.dataframe(
                power_index_df,
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
        st.subheader("Institutional Diagnosis")

        diagnosis = []

        for relation in relations:

            source = relation["source"]
            target = relation["target"]
            relation_type = relation["relation_type"]

            if relation_type == "conflict":
                diagnosis.append(
                    f"{source} berada dalam konflik dengan {target}."
                )

            elif relation_type == "collaboration":
                diagnosis.append(
                    f"{source} membangun kolaborasi dengan {target}."
                )

            elif relation_type == "influence":
                diagnosis.append(
                    f"{source} memberikan pengaruh terhadap {target}."
                )

            elif relation_type == "power":
                diagnosis.append(
                    f"{source} memiliki dominasi kekuasaan terhadap {target}."
                )

        for item in diagnosis:
            st.write("-", item)
    else:
        st.warning("Belum ada aktor terdeteksi.")
        
