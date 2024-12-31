import json
import os
from docx import Document
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
from joblib import dump

def read_docx(file_path):
    """Reads text from a .docx file"""
    doc = Document(file_path)
    return [para.text for para in doc.paragraphs if para.text.strip()]

def save_to_json(data, output_path):
    """Saves data to a JSON file"""
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def save_vectorizer(vectorizer, file_path):
    """Saves CountVectorizer's vocabulary"""
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(vectorizer.vocabulary_, f)

def save_lda_model(lda_model, file_path):
    """Saves the LDA model"""
    dump(lda_model, file_path)

def vectorize_lda(documents, n_topics=2):
    """Transforms documents using LDA"""
    count_vectorizer = CountVectorizer()
    count_matrix = count_vectorizer.fit_transform(documents)
    lda = LatentDirichletAllocation(n_components=n_topics, random_state=42)
    lda_matrix = lda.fit_transform(count_matrix)
    return lda_matrix, count_vectorizer, lda

def main(file_path, output_path, vectorizer_path, lda_model_path, n_topics=50):
    """Reads a .docx file, vectorizes with LDA, and saves results"""
    documents = read_docx(file_path)
    print(f"Extracted {len(documents)} sentences from the document.")
    
    vectors, count_vectorizer, lda = vectorize_lda(documents, n_topics=n_topics)
    
    # Save JSON, vectorizer, and LDA model
    data = {"documents": documents, "vectors": vectors.tolist()}
    save_to_json(data, output_path)
    save_vectorizer(count_vectorizer, vectorizer_path)
    save_lda_model(lda, lda_model_path)
    
    print(f"Results saved to {output_path}")
    print(f"Vectorizer vocabulary saved to {vectorizer_path}")
    print(f"LDA model saved to {lda_model_path}")

# Example execution
if __name__ == "__main__":
    input_file = os.path.join(os.path.dirname(__file__), "data.docx")
    output_file = os.path.join(os.path.dirname(__file__), "output.json")
    vectorizer_file = os.path.join(os.path.dirname(__file__), "vectorizer_vocab.json")
    lda_model_file = os.path.join(os.path.dirname(__file__), "lda_model.joblib")
    main(input_file, output_file, vectorizer_file, lda_model_file, n_topics=50)
