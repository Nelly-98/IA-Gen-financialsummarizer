import streamlit as st
from src.preprocessing import process_text
from src.summarizer import generate_summary
import os

st.title("Générateur de Résumés pour Documents Financiers")

uploaded_file = st.file_uploader("Choisissez un document (PDF ou DOCX)", type=["pdf", "docx"])
if uploaded_file is not None:
    text = process_text(uploaded_file)
    st.write("**Texte extrait :**")
    st.write(text[:1000] + "...")  # Affiche un extrait du texte

    if st.button("Générer le résumé"):
        summary = generate_summary(text)
        st.write("**Résumé :**")
        st.write(summary)
