import sqlite3
import pandas as pd
from crawler.crawler import crawl_page
from analyzer.keyword_tracker import find_keywords
from analyzer.entity_extractor import extract_entities
from dashboard.visualize import visualize_data
from database.db_utils import init_db, save_page, export_to_csv
from logger import setup_logger

def seed_data():
    """Insert sample posts into the database for testing."""
    samples = [
        (
            "http://test.onion/1",
            "This forum post mentions ransomware and bitcoin. Contact: hacker@example.com"
        ),
        (
            "http://test.onion/2",
            "We are selling stolen credit cards. Send payment to 1BoatSLRHtKNngkdXEeobR76b53LETtpyT"
        ),
        (
            "http://test.onion/3",
            "Phishing campaign targeting banks. Server IP: 192.168.1.100"
        ),
        (
            "http://test.onion/4",
            "Zero-day exploit available. Email us at exploit@darkmail.com"
        )
    ]

    for url, content in samples:
        save_page(url, content)

    print("✅ Seed data inserted into darkweb.db")

def run():
    init_db()
    logger = setup_logger()

    # Optional: crawl live onion sites
    urls = [
        "http://duckduckgogg42xjoc72x3sjasowoarfbgcmvfimaftt6twagswzczad.onion"
    ]
    for url in urls:
        text = crawl_page(url)
        if text:
            save_page(url, text)
            logger.info(f"Crawled {url}")

    # 🔑 Analyze all posts in DB (including seeded ones)
    conn = sqlite3.connect("darkweb.db")
    df = pd.read_sql_query("SELECT * FROM posts", conn)
    conn.close()

    for _, row in df.iterrows():
        keywords = find_keywords(row["content"])
        entities = extract_entities(row["content"])
        print(f"URL: {row['url']}")
        print("Keywords:", keywords)
        print("Entities:", entities)

    export_to_csv()
    visualize_data()

if __name__ == "__main__":
    # Seed once for testing
    seed_data()
    run()

