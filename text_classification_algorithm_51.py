# text_classification_algorithm

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report
data = [
    "I love this product",     
    "This is an amazing movie", 
    "I hate this game",        
    "Worst purchase ever",     
    "Best decision I made",   
    "Not worth the money",     
    "Absolutely wonderful!",  
    "Very disappointing",      
]

labels = [1, 1, 0, 0, 1, 0, 1, 0]
X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.3, random_state=42)
vectorizer = CountVectorizer()  
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)
classifier = MultinomialNB()
classifier.fit(X_train_vec, y_train)
y_pred = classifier.predict(X_test_vec)
print("Accuracy: ", accuracy_score(y_test, y_pred))
print("Classification Report: \n", classification_report(y_test, y_pred))

