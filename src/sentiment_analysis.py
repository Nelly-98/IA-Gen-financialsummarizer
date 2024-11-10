from transformers import pipeline

def analyze_sentiment(text):
    sentiment_analyzer = pipeline("sentiment-analysis")
    return sentiment_analyzer(text)