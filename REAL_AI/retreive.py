import json
import os
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.metrics.pairwise import cosine_similarity
from joblib import load

def load_json(file_path):
    """Loads a JSON file"""
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def load_vectorizer(file_path):
    """Loads CountVectorizer's vocabulary"""
    with open(file_path, 'r', encoding='utf-8') as f:
        vocab = json.load(f)
    return CountVectorizer(vocabulary=vocab)

def load_lda_model(file_path):
    """Loads a saved LDA model"""
    return load(file_path)

def find_top_similar_vectors(input_vector, vectors, top_n=5):
    """Finds top N similar vectors to the input vector"""
    similarities = cosine_similarity([input_vector], vectors)[0]
    top_indices = np.argsort(similarities)[::-1][:top_n]
    return [(index, similarities[index]) for index in top_indices]

def main(input_text, json_path, vectorizer_path, lda_model_path, top_n=5):
    """Compares the input text with JSON's vectors and outputs top N similar"""
    # Load JSON data, vectorizer, and LDA model
    data = load_json(json_path)
    documents = data["documents"]
    stored_vectors = np.array(data["vectors"])
    count_vectorizer = load_vectorizer(vectorizer_path)
    lda_model = load_lda_model(lda_model_path)
    
    # Transform the input text
    input_vector = lda_model.transform(count_vectorizer.transform([input_text]))[0]
    
    # Find top similar vectors
    top_similar = find_top_similar_vectors(input_vector, stored_vectors, top_n=top_n)
    
    # Output results
    print("\nTop similar sentences:")
    for rank, (index, similarity) in enumerate(top_similar, 1):
        print(f"{rank}. Similarity: {similarity:.4f}, Sentence: {documents[index]}")

# Example execution
if __name__ == "__main__":
    input_sentence = input("Enter a sentence: ")
    json_file_path = os.path.join(os.path.dirname(__file__), "output.json")
    vectorizer_file = os.path.join(os.path.dirname(__file__), "vectorizer_vocab.json")
    lda_model_file = os.path.join(os.path.dirname(__file__), "lda_model.joblib")
    main(input_sentence, json_file_path, vectorizer_file, lda_model_file, top_n=5)
