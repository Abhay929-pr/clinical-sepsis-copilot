# scripts/nlp_feature_extraction.py
from transformers import pipeline

def extract_entities_from_note(text):
    """Extracts medical entities from a clinical note."""
    # Using a general NER model as an example. 
    # For a real application, a clinical-specific model is recommended.
    nlp_pipeline = pipeline("ner", model="dslim/bert-base-NER", tokenizer="dslim/bert-base-NER")
    
    entities = nlp_pipeline(text)
    symptoms = [e['word'] for e in entities if '##' not in e['word']] # Simple filter
    return {"extracted_symptoms": symptoms}

# Example of how you might use it
if __name__ == '__main__':
    note = "Patient complains of fever and shortness of breath. Administered Tylenol."
    extracted_info = extract_entities_from_note(note)
    print(extracted_info)
