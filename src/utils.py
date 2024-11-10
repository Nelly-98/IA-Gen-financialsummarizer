import os
import pickle

def save_summary_to_file(summary, filename="summary.txt"):
    with open(filename, "w") as file:
        file.write(summary)

def load_sample_documents(path="data/sample_reports/"):
    return [os.path.join(path, f) for f in os.listdir(path) if f.endswith(('.pdf', '.docx'))]

def load_model(model_name):
    model_path = f"models/{model_name}.pkl"
    if not os.path.exists(model_path):
        # Ici, ajouter la logique pour télécharger le modèle depuis une source, ex: Hugging Face
        pass
    with open(model_path, 'rb') as f:
        model = pickle.load(f)
    return model