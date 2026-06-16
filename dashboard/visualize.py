import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from analyzer.keyword_tracker import find_keywords
from analyzer.entity_extractor import extract_entities

def visualize_data():
    conn = sqlite3.connect("darkweb.db")
    df = pd.read_sql_query("SELECT * FROM posts", conn)
    conn.close()

    # Collect keyword and entity counts
    keyword_counts = {}
    entity_counts = {"emails": 0, "btc_wallets": 0, "ips": 0}

    for _, row in df.iterrows():
        kws = find_keywords(row["content"])
        ents = extract_entities(row["content"])

        for kw in kws:
            keyword_counts[kw] = keyword_counts.get(kw, 0) + 1

        for k, v in ents.items():
            entity_counts[k] += len(v)

    # Plot keyword frequencies
    if keyword_counts:
        plt.figure(figsize=(8,5))
        pd.Series(keyword_counts).plot(kind="bar", color="skyblue")
        plt.title("Keyword Frequencies")
        plt.xlabel("Keyword")
        plt.ylabel("Count")
        plt.tight_layout()
        plt.savefig("static/keywords.png", bbox_inches="tight")
        plt.close()

    # Plot entity frequencies
    plt.figure(figsize=(8,5))
    pd.Series(entity_counts).plot(kind="bar", color="salmon")
    plt.title("Entity Frequencies")
    plt.xlabel("Entity Type")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig("static/entities.png", bbox_inches="tight")
    plt.close()

