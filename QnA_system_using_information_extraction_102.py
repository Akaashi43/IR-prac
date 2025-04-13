# QnA_system_using_information_extraction

import string
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
nltk.download('punkt')      
nltk.download('stopwords')  
def preprocess_text(text):
    text = text.translate(str.maketrans("", "", string.punctuation))
    text = text.lower()
    return text
def question_answering_system(question, context):
    context_sentences = nltk.sent_tokenize(context)
    context_sentences_clean = [preprocess_text(sentence) for sentence in context_sentences]
    question_clean = preprocess_text(question)
    tfidf_vectorizer = TfidfVectorizer(stop_words=stopwords.words('english'))
    corpus = [question_clean] + context_sentences_clean
    tfidf_matrix = tfidf_vectorizer.fit_transform(corpus)
    cosine_sim = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:])
    best_match_index = cosine_sim.argmax()
    answer = context_sentences[best_match_index]
    return answer
context = """
Artificial intelligence (AI) is intelligence demonstrated by machines, in contrast to the natural intelligence displayed
by humans and animals. Leading AI textbooks define the field as the study of "intelligent agents": any device that perceives
its environment and takes actions that maximize its chance of successfully achieving its goals.
AI research has been divided into subfields that often fail to communicate with each other.
These include: "robotics", which focuses on practical concerns, "machine learning", which focuses on
the question of how to build machines that learn, and "artificial general intelligence",
which focuses on the question of how to build machines that can perform any intellectual task that a human being can.
"""
question = "What is artificial intelligence?"
answer = question_answering_system(question, context)
print("Answer:", answer)
