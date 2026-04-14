import re
from collections import Counter

STOPWORDS = {"the","and","for","with"}

def clean_text(text):
    return re.sub(r"\s+", " ", text).strip()

def tokenize(text):
    return re.findall(r"[a-zA-Z]+", text.lower())

def extract_keywords(text, limit=20):
    words = tokenize(text)
    freq = Counter(words)
    return [w for w,_ in freq.most_common(limit) if w not in STOPWORDS]
