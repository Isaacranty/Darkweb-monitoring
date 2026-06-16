from bs4 import BeautifulSoup
import requests
from database.db_utils import save_page
from crawler.tor_utils import proxies

def crawl_page(url):
    try:
        page = requests.get(url, proxies=proxies, timeout=30)
        soup = BeautifulSoup(page.content, "html.parser")
        save_page(url, soup.get_text())
        return soup.get_text()
    except Exception as e:
        print(f"Error crawling {url}: {e}")
        return ""
