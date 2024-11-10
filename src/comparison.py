from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

def compare_summaries(new_summary, existing_summaries):
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([new_summary] + existing_summaries)
    similarities = cosine_similarity(vectors[0:1], vectors[1:]).flatten()
    return similarities
