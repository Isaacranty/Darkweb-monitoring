from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route("/")
def dashboard():
    conn = sqlite3.connect("darkweb.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, url, content FROM posts")
    posts = [{"id": row[0], "url": row[1], "content": row[2]} for row in cursor.fetchall()]
    conn.close()

    return render_template("dashboard.html", posts=posts)
