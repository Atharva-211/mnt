from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def similarity_score(doc1, doc2):
    vectorizer = TfidfVectorizer()
    tfidf = vectorizer.fit_transform([doc1, doc2])
    similarity = cosine_similarity(tfidf[0:1], tfidf[1:2])
    return similarity[0][0]

# Example usage
doc1 = "I love machine learning"
doc2 = "i Love Machine Learning"
print("Similarity Score:", similarity_score(doc1, doc2))
