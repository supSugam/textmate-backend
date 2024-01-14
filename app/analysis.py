from nltk.sentiment import SentimentIntensityAnalyzer

def perform_sentiment_analysis(text):
    # Initialize the Sentiment Intensity Analyzer
    sid = SentimentIntensityAnalyzer()

    # Perform sentiment analysis on the text
    sentiment_scores = sid.polarity_scores(text)

    # Classify sentiment based on the compound score
    sentiment_label = 'Positive' if sentiment_scores['compound'] >= 0 else 'Negative'

    return sentiment_label
