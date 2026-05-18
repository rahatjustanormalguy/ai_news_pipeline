# AI News Pipeline

An automated ETL pipeline that tracks AI model releases and tech news in real time.

## What it does
- Fetches live AI news from NewsAPI
- Cleans and transforms data using Pandas
- Stores articles in a PostgreSQL database
- Queryable with SQL for analysis

## Tech Stack
- Python 3.9
- Pandas
- PostgreSQL 18
- psycopg2
- NewsAPI

## Pipeline Steps
1. `fetch_news.py` — fetches raw articles from NewsAPI
2. `transform_news.py` — cleans and shapes data with Pandas
3. `load_to_db.py` — loads transformed data into PostgreSQL

## Setup
1. Clone the repo
2. Install dependencies: `pip3 install pandas requests psycopg2-binary python-dotenv`
3. Create a `.env` file with your API key: `NEWS_API_KEY=your_key_here`
4. Create a PostgreSQL database called `ai_news`
5. Run: `python3 load_to_db.py`

## Author
BSc IT Student — building toward a Data Engineering career
