import pandas as pd
import requests
import os
import psycopg2
from dotenv import load_dotenv

# Load API key
load_dotenv()
api_key = os.getenv("NEWS_API_KEY")

# # Fetch data(update1.0)
# query = "AI model release"
# url = f"https://newsapi.org/v2/everything?q={query}&language=en&sortBy=publishedAt&apiKey={api_key}"
# response = requests.get(url)
# data = response.json()
topics = [
    "AI model release",
    "large language model",
    "OpenAI",
    "Google Gemini",
    "machine learning"
]

all_articles = []

for topic in topics:
    url = f"https://newsapi.org/v2/everything?q={topic}&language=en&sortBy=publishedAt&pageSize=20&apiKey={api_key}"
    response = requests.get(url)
    data = response.json()
    if data['status'] == 'ok':
        all_articles.extend(data['articles'])

data = {'articles': all_articles}


# Transform data
df = pd.DataFrame(data['articles'])
df = df[['title', 'source', 'publishedAt', 'url', 'description']]
df['source'] = df['source'].apply(lambda x: x['name'])
df.columns = ['title', 'source', 'published_at', 'url', 'description']
df = df.dropna(subset=['title'])

# Connect to PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="ai_news",
    user="postgres",
    password="2026"
)

cursor = conn.cursor()

# Create table if it doesn't exist
cursor.execute("""
    CREATE TABLE IF NOT EXISTS articles (
        id SERIAL PRIMARY KEY,
        title TEXT,
        source TEXT,
        published_at TEXT,
        url TEXT,
        description TEXT
    )
""")

# # Insert articles
# for _, row in df.iterrows():
#     cursor.execute("""
#         INSERT INTO articles (title, source, published_at, url, description)
#         VALUES (%s, %s, %s, %s, %s)
#     """, (row['title'], row['source'], row['published_at'], row['url'], row['description']))

# conn.commit()
# cursor.close()
# conn.close()

# print(f"Done! {len(df)} articles saved to database.")

# Insert articles (skip duplicates)
inserted = 0
skipped = 0
for _, row in df.iterrows():
    cursor.execute("SELECT id FROM articles WHERE url = %s", (row['url'],))
    exists = cursor.fetchone()
    if not exists:
        cursor.execute("""
            INSERT INTO articles (title, source, published_at, url, description)
            VALUES (%s, %s, %s, %s, %s)
        """, (row['title'], row['source'], row['published_at'], row['url'], row['description']))
        inserted += 1
    else:
        skipped += 1

conn.commit()
cursor.close()
conn.close()

print(f"Done! {inserted} new articles inserted, {skipped} duplicates skipped.")
