
import json
def load_data(file):
    with open(file, "r", encoding="utf-8") as f:
        data = json.load(f)
    return (data)




def generate_better_characters(file):
    data = load_data(file)
    print (len(data))
    new_characters = []
    for item in data:
        new_characters.append(item)
    for item in data:
        item = item.replace("The", "").replace("the", "").replace("and", "").replace("And", "")
        names = item.split(" ")
        for name in names:
            name = name.strip()
            new_characters.append(name)
        if "(" in item:
            names = item.split("(")
            for name in names:
                name = name.replace(")", "").strip()
                new_characters.append(name)
        if "," in item:
            names = item.split(",")
            for name in names:
                name = name.replace("and", "").strip()
                if " " in name:
                    new_names = name.split()
                    for x in new_names:
                        x = x.strip()
                        new_characters.append(x)
                new_characters.append(name)
    print (len(new_characters))
    final_characters = []
    titles = ["Dr.", "Professor", "Mr.", "Mrs.", "Ms.", "Miss", "Aunt", "Uncle", "Mr. and Mrs."]
    for character in new_characters:
        if "" != character:
            final_characters.append(character)
            for title in titles:
                titled_char = f"{title} {character}"
                final_characters.append(titled_char)


    print (len(final_characters))
    final_characters = list(set(final_characters))
    print (len(final_characters))
    final_characters.sort()
    return (final_characters)


