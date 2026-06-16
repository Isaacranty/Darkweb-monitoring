import re

def extract_entities(text):
    entities = {}
    # Emails
    entities["emails"] = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-z]{2,}", text)
    # Bitcoin wallets
    entities["btc_wallets"] = re.findall(r"\b[13][a-km-zA-HJ-NP-Z1-9]{25,34}\b", text)
    # IP addresses
    entities["ips"] = re.findall(r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b", text)
    return entities

