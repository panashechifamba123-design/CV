from utils.text_tools import extract_keywords, tokenize

def score_match(job_text, cv_text):
    job_keywords = extract_keywords(job_text)
    cv_tokens = set(tokenize(cv_text))
    matched = [k for k in job_keywords if k in cv_tokens]
    missing = [k for k in job_keywords if k not in cv_tokens]
    score = int(len(matched)/max(len(job_keywords),1)*100)
    return score, matched, missing, missing

def build_tailored_cv(job_text, cv_text):
    return cv_text

def create_change_log(missing):
    return []
