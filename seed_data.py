from database.db_utils import init_db, save_page

def seed():
    init_db()

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

if __name__ == "__main__":
    seed()
