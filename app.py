import streamlit as st
from src.preprocessing import process_text
from src.summarizer import generate_summary
from src.utils import load_model
from src.sentiment_analysis import analyze_sentiment
from src.comparison import compare_summaries
#from src.table_extraction import extract_tables
import os
from datetime import datetime
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Création de la sidebar pour les options
st.sidebar.title("Options")

# Choix de la longueur du résumé
summary_length = st.sidebar.slider("Longueur du résumé (mots)", 50, 500, 150, step=50)

# Options de prétraitement
remove_numbers = st.sidebar.checkbox("Supprimer les chiffres")
remove_stopwords = st.sidebar.checkbox("Supprimer les mots courants")

# Choix du modèle de résumé
model_choice = st.sidebar.selectbox("Modèle de résumé", ["facebook/bart-large-cnn", "t5-small", "google/pegasus-xsum"])

# Affichage du titre principal
st.title("Générateur de Résumés pour Documents Financiers")

# Fonction de téléchargement de fichier
uploaded_file = st.file_uploader("Choisissez un document (PDF ou DOCX)", type=["pdf", "docx"])

# Traitement si un fichier est chargé
if uploaded_file is not None:
    # Extraction et affichage du texte
    text = process_text(uploaded_file)
    st.write("**Texte extrait :**")
    st.write(text[:1000] + "...")  # Affiche un extrait du texte

    # Bouton de génération du résumé
    if st.button("Générer le résumé"):
        summary = generate_summary(text, model_name=model_choice, max_length=summary_length)
        st.write("**Résumé :**")
        st.write(summary)

        # Sauvegarde du texte et du résumé généré
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        model_info = model_choice.replace("/", "_").replace(":", "_")
        summary_length = str(summary_length) 
        # Enregistrement du texte extrait
        with open(f"data/processed_data/extracted_text_{timestamp}.txt", "w") as f:
            f.write(text)

        # Enregistrement du résumé avec des informations sur le modèle et la longueur
        with open(f"outputs/summary_{model_info}_{summary_length}_{timestamp}.txt", "w") as f:
            f.write(f"Modèle utilisé: {model_info}\nLongueur du résumé: {summary_length} mots\n\n")
            f.write(summary)

        st.success("Résumé et texte extraits sauvegardés.")

        # Option de téléchargement
        st.download_button("Télécharger le résumé", data=summary, file_name="summary.txt", mime="text/plain")

    
# Sidebar pour les fonctionnalités supplémentaires
st.sidebar.title("Fonctionnalités supplémentaires")
# Affichage du nuage de mots si l'option est activée
if st.sidebar.checkbox("Afficher un nuage de mots des concepts clés"):
    wordcloud = WordCloud(width=800, height=400).generate(text)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    st.pyplot(plt)

# Analyse de sentiments
if st.sidebar.checkbox("Analyser le sentiment"):
    sentiment = analyze_sentiment(text)
    st.write("**Sentiment :**", sentiment)

# Comparaison avec d'autres résumés (à condition d'avoir d'autres résumés disponibles)
if st.sidebar.checkbox("Comparer avec d'autres résumés"):
    existing_summaries = ["Résumé 1", "Résumé 2", "Résumé 3"]  # Exemple pour démonstration
    similarities = compare_summaries(summary, existing_summaries)
    st.write("**Similarité avec d'autres résumés :**", similarities)

# Extraction de tableaux pour les fichiers PDF
#if uploaded_file.type == "application/pdf":
    #tables = extract_tables(uploaded_file)
    #for i, table in enumerate(tables):
        #st.write(f"**Tableau {i + 1} :**")
        #st.dataframe(table)
