from transformers import pipeline

# Chargement du pipeline de résumé
summarizer = pipeline("summarization")

def generate_summary(text, max_length=150):
    # Génère le résumé en utilisant le modèle NLP
    summary = summarizer(text, max_length=max_length, min_length=50, do_sample=False)
    return summary[0]['summary_text']
