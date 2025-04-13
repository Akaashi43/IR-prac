# inverted_index_construction_algorithm

import string
def tokenize(text):
    """Convert the text to lowercase, remove punctuation, and split into words."""
    text = text.lower()  
    text = text.translate(str.maketrans('', '', string.punctuation))  
    return text.split()  
def build_inverted_index(documents):
    """Build an inverted index from a list of documents."""
    inverted_index = {}
    for doc_id, doc in enumerate(documents):
        words = tokenize(doc)
        
        for word in words:
            if word not in inverted_index:
                inverted_index[word] = []
            if doc_id not in inverted_index[word]:
                inverted_index[word].append(doc_id)
    return inverted_index
documents = [
    "The quick brown fox jumps over the lazy dog.",
    "A fox is quick and brown.",
    "The lazy dog sleeps all day."
]
inverted_index = build_inverted_index(documents)
for term, doc_ids in inverted_index.items():
    print(f"{term}: {doc_ids}")
