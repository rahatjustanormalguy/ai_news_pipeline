import pandas as pd
import requests
import os
from dotenv import load_dotenv

# Load API key
load_dotenv()
api_key = os.getenv("NEWS_API_KEY")

# Fetch data
query = "AI model release"
url = f"https://newsapi.org/v2/everything?q={query}&language=en&sortBy=publishedAt&apiKey={api_key}"
response = requests.get(url)
data = response.json()

# Put articles into a Pandas DataFrame
df = pd.DataFrame(data['articles'])

# Keep only the columns we care about
df = df[['title', 'source', 'publishedAt', 'url', 'description']]

# Extract source name from the source column
df['source'] = df['source'].apply(lambda x: x['name'])

# Rename columns to clean names
df.columns = ['title', 'source', 'published_at', 'url', 'description']

# Drop any rows with missing titles
df = df.dropna(subset=['title'])

# Show the first 5 rows
print(df.head())
print(f"\nShape: {df.shape}")
