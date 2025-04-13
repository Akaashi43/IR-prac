# simple_dociment_retrieval

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
def retrieve_documents(query, inverted_index, documents):
    """Retrieve documents based on the query using the inverted index."""
    query_terms = tokenize(query)
    doc_sets = []
    for term in query_terms:
        if term in inverted_index:
            doc_sets.append(set(inverted_index[term]))
        else:
            return []
    result_set = set.intersection(*doc_sets)
    result_documents = [documents[doc_id] for doc_id in result_set]
    return result_documents
documents = [
    "The quick brown fox jumps over the lazy dog.",
    "A fox is quick and brown.",
    "The lazy dog sleeps all day."
]
inverted_index = build_inverted_index(documents)
query = "quick fox"
retrieved_docs = retrieve_documents(query, inverted_index, documents)
print("Retrieved documents:")
for doc in retrieved_docs:
    print(f"- {doc}")
