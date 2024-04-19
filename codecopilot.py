import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import NMF
import os

def load_text(filename):
    """ Load text from a file. """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print("Error: File not found.")
        return None

def preprocess_text(text):
    """ Preprocess text using spaCy for NLP tasks. """
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(text)
    processed_text = ' '.join([token.lemma_ for token in doc if not token.is_stop and not token.is_punct])
    return processed_text

def extract_keywords(text, n_keywords=10):
    """ Extract keywords using TF-IDF. """
    vectorizer = TfidfVectorizer(max_features=1000)
    tfidf_matrix = vectorizer.fit_transform([text])
    feature_names = vectorizer.get_feature_names_out()
    sorted_items = sorted(list(zip(vectorizer.idf_, feature_names)), reverse=True)
    keywords = [item[1] for item in sorted_items[:n_keywords]]
    return keywords

def generate_summary(text, n_topics=5, n_top_words=10):
    """ Generate text summary using NMF for topic modeling. """
    vectorizer = TfidfVectorizer(max_features=2000, stop_words='english')
    X = vectorizer.fit_transform([text])
    nmf = NMF(n_components=n_topics, random_state=42)
    W = nmf.fit_transform(X)
    H = nmf.components_
    feature_names = vectorizer.get_feature_names_out()
    topics = []
    for topic_idx, topic in enumerate(H):
        top_features_ind = topic.argsort()[:-n_top_words - 1:-1]
        top_features = [feature_names[i] for i in top_features_ind]
        topics.append(" ".join(top_features))
    return ' | '.join(topics)

def main():
    filename = input("Enter the file path of the text document: ")
    text = load_text(filename)
    if text:
        processed_text = preprocess_text(text)
        keywords = extract_keywords(processed_text)
        summary = generate_summary(processed_text)
        print("Keywords:", keywords)
        print("Summary:", summary)

if __name__ == '__main__':
    main()
