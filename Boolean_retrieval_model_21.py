# Boolean_retrieval_model
import string
def tokenize(text):
    """Convert the text to lowercase, remove punctuation, and split into words."""
    text = text.lower()  
    text = text.translate(str.maketrans('', '', string.punctuation))  # Remove punctuation
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
def boolean_retrieve(query, inverted_index, documents):
    """Retrieve documents based on the Boolean query using the inverted index."""
    query = query.lower()
    query_terms = tokenize(query)
    result_set = None
    operator = None  
    for term in query_terms:
        if term == "and":
            operator = "AND"
        elif term == "or":
            operator = "OR"
        elif term == "not":
            operator = "NOT"
        else:
            if operator == "AND":
                if result_set is None:
                    result_set = set(inverted_index.get(term, []))
                else:
                    result_set &= set(inverted_index.get(term, []))
            elif operator == "OR":
                if result_set is None:
                    result_set = set(inverted_index.get(term, []))
                else:
                    result_set |= set(inverted_index.get(term, []))
            elif operator == "NOT":
                result_set -= set(inverted_index.get(term, []))
            else:
                if result_set is None:
                    result_set = set(inverted_index.get(term, []))
                else:
                    result_set &= set(inverted_index.get(term, []))
            operator = None  
    result_documents = [documents[doc_id] for doc_id in result_set] if result_set else []
    return result_documents
documents = [
    "The quick brown fox jumps over the lazy dog.",
    "A fox is quick and brown.",
    "The lazy dog sleeps all day."
]
inverted_index = build_inverted_index(documents)
queries = [
    "quick and fox",    
    "quick or dog",     
    "quick and not lazy"  
]
for query in queries:
    print(f"Query: {query}")
    retrieved_docs = boolean_retrieve(query, inverted_index, documents)
    print("Retrieved documents:")
    for doc in retrieved_docs:
        print(f"- {doc}")
    print()
