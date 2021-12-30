
import spacy
from gen_model import test_model, save_data

if __name__ == "__main__":
    # load the generated model
    nlp = spacy.load("model/hp_ner")
    ie_data = {}
    with open ("data/hp.txt", "r")as f:
        text = f.read()

        chapters = text.split("CHAPTER")[1:]
        for chapter in chapters:
            chapter_num, chapter_title = chapter.split("\n\n")[0:2]
            chapter_num = chapter_num.strip()
            segments = chapter.split("\n\n")[2:]
            hits = []
            for segment in segments:
                segment = segment.strip()
                segment = segment.replace("\n", " ")
                results = test_model(nlp, segment)
                for result in results:
                    hits.append(result)
            ie_data[chapter_num] = hits

    save_data("data/hp_data.json", ie_data)

        
