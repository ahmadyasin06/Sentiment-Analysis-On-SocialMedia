from textblob import TextBlob

class SentimentAnalyzer:
    def analyze(self, text):
        blob = TextBlob(text)
        polarity = blob.sentiment.polarity

        if polarity > 0:
            label = "Positive"
        elif polarity < 0:
            label = "Negative"
        else:
            label = "Neutral"

        confidence = round(abs(polarity) * 100, 2)

        return {
            "label": label,
            "polarity": polarity,
            "confidence": confidence
        }
