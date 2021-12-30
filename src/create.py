from src.generate_name_list import generate_better_characters

def create_training_data(file, type):
    data = generate_better_characters(file)
    patterns = []
    for item in data:
        pattern = {
                    "label": type,
                    "pattern": item
                    }
        patterns.append(pattern)
    return patterns
