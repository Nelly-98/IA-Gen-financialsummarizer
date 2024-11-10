# Générateur de Résumés Automatisés pour Documents Financiers

## Description
Ce projet a pour objectif de créer un générateur de résumés automatisés pour des documents financiers (ex. : rapports annuels, bilans). Le projet utilise des modèles de traitement du langage naturel (NLP) et est construit avec Python et Streamlit pour une interface utilisateur simple.

## Fonctionnalités
- Extraction et traitement de texte depuis des documents financiers (PDF, DOCX)
- Génération de résumés concis à l'aide de modèles NLP pré-entraînés
- Interface utilisateur via Streamlit pour charger des documents et afficher les résumés

## Structure du projet
- **data/** : Contient les documents d'exemple et les fichiers de données transformés.
- **src/** : Scripts principaux, comprenant le prétraitement, la génération de résumé, l'analyse des sentiments et les utilitaires.
- **outputs/** : Stocke les résumés générés.
- **notebooks/** : Notebooks pour l'exploration et les tests initiaux.

## Prérequis
- Python 3.8 ou plus
- Environnement virtuel (recommandé)

## Installation
1. Clonez ce dépôt :
   ```bash
   git clone https://github.com/Nelly-98/financial-summarizer.git
   cd financial-summarizer

2. Créez un environnement virtuel et activez-le :
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # Sur Linux/macOS
    venv\Scripts\activate     # Sur Windows

3. Installez les dépendances :
    ```bash
    pip install -r requirements.txt

## Utilisation
1. Placez les documents financiers que vous souhaitez résumer dans le dossier 
    ```bash
    data/sample_reports/.

2. Lancez l'application Streamlit :
    ```bash
    streamlit run src/app.py

3. Suivez les instructions à l'écran pour charger un document, choisir le model à utiliser et générer un résumé.

## Auteur
Nelly Guepnang
