import requests
from bs4 import BeautifulSoup

def fetch_job_posting(url):
    if not url:
        return ""
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    for tag in soup(["script","style"]):
        tag.decompose()
    return soup.get_text("\n")
