#  spelling_correction_model into information rs

from spellchecker import SpellChecker
documents = [
    "I have a laptop with a good processor.",
    "The laptop is very useful for coding and gaming.",
    "I need a new smartphone."
]
def simple_search(query, documents):
    return [doc for doc in documents if query.lower() in doc.lower()]
def correct_spelling(query):
    spell = SpellChecker()
    return " ".join([spell.correction(word) for word in query.split()])
def search_with_spelling_correction(query, documents):
    corrected_query = correct_spelling(query)
    print(f"Original Query: {query}")
    print(f"Corrected Query: {corrected_query}")
    results = simple_search(corrected_query, documents)
    if results:
        print("Results:", results)
    else:
        print("No results found.")
search_with_spelling_correction("I want to get a laptoop.", documents)
