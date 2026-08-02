from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from textblob import TextBlob

analyzer = SentimentIntensityAnalyzer()

def analyze_sentiment(text: str) -> dict:
    """
    Analyzes sentiment and emotional metrics from input text.
    Returns polarity, subjectivity, sentiment score, and category.
    """
    if not text or not text.strip():
        return {
            "compound": 0.0,
            "pos": 0.0,
            "neu": 1.0,
            "neg": 0.0,
            "polarity": 0.0,
            "subjectivity": 0.0,
            "label": "Neutral",
            "emoji": "😐"
        }
    
    # VADER analysis
    vader_scores = analyzer.polarity_scores(text)
    
    # TextBlob analysis
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity
    
    compound = vader_scores["compound"]
    
    if compound >= 0.05:
        label = "Positive"
        emoji = "😃"
    elif compound <= -0.05:
        label = "Negative"
        emoji = "😔"
    else:
        label = "Neutral"
        emoji = "😐"
        
    return {
        "compound": round(compound, 3),
        "pos": round(vader_scores["pos"] * 100, 1),
        "neu": round(vader_scores["neu"] * 100, 1),
        "neg": round(vader_scores["neg"] * 100, 1),
        "polarity": round(polarity, 3),
        "subjectivity": round(subjectivity, 3),
        "label": label,
        "emoji": emoji
    }
