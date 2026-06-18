import sqlite3
import os
import random
import re
from ml.sentiment_analyzer import SentimentAnalyzer

class DataHandler:
    def __init__(self):
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.db_path = os.path.join(base_dir, "database", "sentiment.db")
        self.analyzer = SentimentAnalyzer()

        print("USING DB:", self.db_path)

    def fetch_post_from_db(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute("SELECT id, content FROM posts")
        posts = cursor.fetchall()

        conn.close()

        print("POSTS FOUND:", posts)

        if not posts:
            return None

        # return only text
        return random.choice(posts)[1]

    def preprocess(self, text):
        text = text.lower()
        text = re.sub(r"http\S+", "", text)
        text = re.sub(r"[^a-zA-Z\s]", "", text)
        return text.strip()

    def process(self, text):
        cleaned_text = self.preprocess(text)
        return self.analyzer.analyze(cleaned_text)
