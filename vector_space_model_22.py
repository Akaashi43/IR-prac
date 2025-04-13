# vector_space_model

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
documents = [
    "The cat sat on the mat.",
    "The dog sat on the mat.",
    "The cat is on the mat.",
    "The dog is in the garden."
]
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(documents)
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
print("Cosine Similarity Matrix:")
print(cosine_sim)
print("\nCosine similarity between Document 1 and Document 2: ", cosine_sim[0][1])
