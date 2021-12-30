import spacy
from spacy.lang.en import English
from spacy.pipeline import EntityRuler
import json
from src.create import create_training_data

def save_data(file, data):
    with open (file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

def generate_rules(patterns):
    nlp = English()
    entity_ruler = nlp.add_pipe("entity_ruler")
    entity_ruler.initialize(lambda: [], nlp=nlp, patterns=patterns)
    nlp.to_disk("model/hp_ner")

def test_model(model, text):
    doc = model(text)
    results = []
    for ent in doc.ents:
        results.append(ent.text)
    return results

if __name__ == "__main__":
    patterns = create_training_data("data/hp_characters.json", "PERSON")
    generate_rules(patterns)
