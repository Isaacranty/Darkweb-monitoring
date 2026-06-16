from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
    <body>
        <h1>Darkweb Monitoring Dashboard</h1>
        <p>Welcome to your monitoring dashboard.</p>
        <a href="/charts">View Charts</a>
    </body>
    </html>
    """

@app.route("/charts")
def charts():
    return """
    <html>
    <body>
        <h2>Keyword Frequencies</h2>
        <img src="/static/keywords.png" width="600">
        <h2>Entity Frequencies</h2>
        <img src="/static/entities.png" width="600">
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
