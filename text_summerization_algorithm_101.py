# text_summerization_algorithm

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
def extractive_summary(text, top_n=3):
    sentences = nltk.sent_tokenize(text)
    sentences_clean = [preprocess_text(sentence) for sentence in sentences]
    tfidf_vectorizer = TfidfVectorizer(stop_words=stopwords.words('english'))
    tfidf_matrix = tfidf_vectorizer.fit_transform(sentences_clean)
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
    sentence_scores = cosine_sim.sum(axis=1)
    ranked_sentences = [sentences[i] for i in sentence_scores.argsort()[-top_n:][::-1]]
    summary = ' '.join(ranked_sentences)
    return summary
text = """
Artificial intelligence (AI) is intelligence demonstrated by machines, in contrast to the natural intelligence displayed by humans and animals.
Leading AI textbooks define the field as the study of "intelligent agents": any device that perceives
its environment and takes actions that maximize its chance of successfully achieving its goals. 
As machines become increasingly capable, tasks considered to require "intelligence" are often removed from the definition of AI,
a phenomenon known as the AI effect."""
summary = extractive_summary(text, top_n=3)
print("Extractive Summary:")
print(summary)
