import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "database", "sentiment.db")

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    content TEXT
)
""")

cursor.execute("DELETE FROM posts")

sample_posts = [
    ("SMEC’26 — Just 1 Day to Go! ✨",),
    ("SMEC’26 — PASSES SOLD OUT!",),
    ("The product was delivered today.",),
    ("SMEC’26 BADGE CEREMONY MOMENT!",),
    ("I am not happy with the experience.",),
    ("Proud to welcome FollicleLove as an Esteemed Sponsor for SMEC’26",),
    ("HAVE YOU REGISTERED YET? ",),
    ("SMEC TANK — Pitch Deck Competition",),
    ("Meet the faces behind SMEC’26! ✨",)
]

cursor.executemany(
    "INSERT INTO posts (content) VALUES (?)",
    sample_posts
)

conn.commit()
conn.close()

print("Database setup completed successfully.")
