def find_keywords(text):
    keywords = ["ransomware", "malware", "bitcoin", "hack", "exploit", "zero-day", "carding", "phishing"]
    found = [kw for kw in keywords if kw in text.lower()]
    return found
