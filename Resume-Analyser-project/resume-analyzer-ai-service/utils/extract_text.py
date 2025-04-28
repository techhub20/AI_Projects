import spacy
from collections import Counter
import re

# Load spacy model for text processing
nlp = spacy.load("en_core_web_sm")

EXCLUDED_WORDS = set([
    "love", "feel", "afraid", "real", "similar", "easy", "confident", "comfortable",
    "solid", "know", "their", "your", "like", "good", "bad", "well", "how", "also",
    "have", "make", "take", "give", "use", "do", "get", "want", "need", "work", "can",
    "using", "ability", "way", "thing", "part", "type", "kind", "much", "many", "talk"
])

ALLOWED_POS = {"NOUN", "PROPN", "ADJ", "VERB"}

SKILLS_MAPPING = {
    "datum": "data", "javascript": "js", "typescript": "ts", "python": "python",
    "sql": "sql", "react": "react", "node": "node.js", "ui": "UI", "ux": "UX",
    "api": "API", "aws": "AWS", "amazon web service": "AWS", "azure": "Azure",
    "google cloud": "GCP", "gcp": "GCP", "docker": "Docker", "kubernetes": "Kubernetes",
    "k8s": "Kubernetes", "machine learning": "ML", "ml": "ML", "artificial intelligence": "AI",
    "ai": "AI", "deep learning": "deep learning", "neural network": "neural networks",
    "big data": "big data", "data analysis": "data analysis", "data science": "data science"
}

def normalize_keyword(keyword):
    keyword = keyword.lower()
    for k, v in SKILLS_MAPPING.items():
        if k in keyword:
            return v
    return keyword

def extract_keywords(text):
    doc = nlp(text.lower())
    keywords = []

    for token in doc:
        if (not token.is_alpha or len(token.text) < 3 or 
            token.pos_ not in ALLOWED_POS or token.lemma_ in EXCLUDED_WORDS):
            continue
        normalized = normalize_keyword(token.lemma_)
        if normalized not in EXCLUDED_WORDS:
            keywords.append(normalized)

    for chunk in doc.noun_chunks:
        if len(chunk.text.split()) > 1:
            normalized_phrase = ' '.join(normalize_keyword(t.lemma_) for t in chunk)
            if normalized_phrase not in EXCLUDED_WORDS:
                keywords.append(normalized_phrase)

    return list(set(keywords))
