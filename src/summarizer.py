from transformers import pipeline

# Fonction pour générer un résumé avec le modèle sélectionné
def generate_summary(text, model_name="facebook/bart-large-cnn", max_length=150):
    # Chargement du pipeline de résumé avec le modèle spécifié
    summarizer = pipeline("summarization", model=model_name)
    # Génération du résumé
    summary = summarizer(text, max_length=max_length, min_length=50, do_sample=False)
    return summary[0]['summary_text']
