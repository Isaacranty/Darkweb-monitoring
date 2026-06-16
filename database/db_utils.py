import sqlite3
import pandas as pd

def init_db():
    conn = sqlite3.connect("darkweb.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            url TEXT,
            content TEXT
        )
    """)
    conn.commit()
    conn.close()

def save_page(url, content):
    conn = sqlite3.connect("darkweb.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO posts (url, content) VALUES (?, ?)", (url, content))
    conn.commit()
    conn.close()

def export_to_csv(filename="report.csv"):
    conn = sqlite3.connect("darkweb.db")
    df = pd.read_sql_query("SELECT * FROM posts", conn)
    df.to_csv(filename, index=False)
    conn.close()

