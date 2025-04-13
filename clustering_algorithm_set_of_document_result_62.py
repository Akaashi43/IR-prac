# clustering_algorithm_set_of_document_result

import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score, adjusted_rand_score, pairwise_distances_argmin_min
documents = [
    "I love programming in Python",
    "Python is great for data science",
    "Data science is fun and interesting",
    "I enjoy hiking in the mountains",
    "Hiking is a great outdoor activity",
    "Mountains are beautiful for trekking"
]
vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(documents)
n_clusters = 2  
kmeans = KMeans(n_clusters=n_clusters, random_state=42)
kmeans.fit(X)
print(f"Inertia: {kmeans.inertia_}")
silhouette_avg = silhouette_score(X, kmeans.labels_)
print(f"Silhouette Score: {silhouette_avg}")
true_labels = [0, 0, 0, 1, 1, 1]
ari = adjusted_rand_score(true_labels, kmeans.labels_)
print(f"Adjusted Rand Index: {ari}")
distances = pairwise_distances_argmin_min(X, kmeans.cluster_centers_)
print(f"Pairwise Distances to Cluster Centers: {distances}")
