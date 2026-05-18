import requests
import os
from dotenv import load_dotenv

# Load the API key from .env file
load_dotenv()
api_key = os.getenv("NEWS_API_KEY")

# What we're searching for
query = "AI model release"
url = f"https://newsapi.org/v2/everything?q={query}&language=en&sortBy=publishedAt&apiKey={api_key}"

# Fetch the data
response = requests.get(url)
data = response.json()

# Print how many articles we got
print(f"Status: {data['status']}")
print(f"Total articles found: {data['totalResults']}")

# Print first 3 articles
for article in data['articles'][:3]:
    print("---")
    print(f"Title: {article['title']}")
    print(f"Source: {article['source']['name']}")
    print(f"Published: {article['publishedAt']}")
