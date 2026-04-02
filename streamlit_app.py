import streamlit as st
from pathlib import Path
import tempfile

from src.rag import answer_question

st.set_page_config(page_title="RAG Chatbot", layout="wide")

st.title("Récupération Génération augmentée")

col1, col2 = st.columns([1, 2])

with col1:
    st.header("Chargeur de données")
    uploaded_file = st.file_uploader("Chargez vos fichiers PDF", type=["pdf"])

with col2:
    st.header("Chatbot")
    question = st.text_input("Posez votre question")

    if st.button("Soumettre"):
        if uploaded_file is None:
            st.warning("Veuillez d'abord charger un fichier PDF.")
        elif not question.strip():
            st.warning("Veuillez saisir une question.")
        else:
            try:
                with tempfile.TemporaryDirectory() as tmpdir:
                    pdf_path = Path(tmpdir) / uploaded_file.name

                    with open(pdf_path, "wb") as f:
                        f.write(uploaded_file.read())

                    st.info("Traitement du document en cours...")

                    response = answer_question(
                        question=question,
                        data_dir=tmpdir
                    )

                    st.subheader("Réponse")
                    st.write(response)

            except Exception as e:
                st.error(f"Erreur : {e}")