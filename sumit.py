from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def analyze_sentment_textblob(text):
    sentiment = TextBlob(text).sentiment.polarity

    if sentiment>0:
        return "positive 😊"
    elif sentiment<0:
        return "negative 😡"
    else:
        return "neutral 😐"

def analyze_sentment_vader(text):
    analyzer = SentimentIntensityAnalyzer()
    Sentiment = analyzer.polarity_scores(text)['compound']
    if Sentiment>0.05:
        return "positive 😊"
    elif Sentiment<-0.05:
        return "negative 😡"
    else:
        return "neutral 😐"
def analyze_input():
    text=input("Enter a sentense: ")
    print(f"text blob sentiment:{analyze_sentment_textblob(text)}")
    print(f"vader sentiment:{analyze_sentment_vader(text)}")

analyze_input()