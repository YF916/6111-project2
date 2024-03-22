import spacy
import requests
import googleapiclient.discovery
import os
import google.generativeai as genai

# Load spaCy model
nlp = spacy.load("en_core_web_lg")

# Function to extract named entities and sentences using spaCy
def extract_entities_and_sentences(text):
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    sentences = [sent.text for sent in doc.sents]
    return entities, sentences

# Example usage
text = "Apple Inc. is planning to open a new store in New York City. The CEO, Tim Cook, announced the news yesterday."

entities, sentences = extract_entities_and_sentences(text)

print("Named Entities:")
for entity in entities:
    print(entity)

print("\nSentences:")
for sentence in sentences:
    print(sentence)