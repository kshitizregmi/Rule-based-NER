# Named Entity Recognition(NER) Using spaCy EntityRuler

A named entity is a “real-world object” that’s assigned a name – for example, a person, a country, a product or a book title. 

For example, for a text: `Apple is looking at buying U.K. startup for $1 billion.`
|Text   |Start| End |Label  |Description|
| ----------- | ----------- | ----------- | ----------- |----------- |
Apple   |0  |5  |ORG    |Companies, agencies, institutions.|
U.K.    |27 |31 |   GPE |Geopolitical entity, i.e. countries, cities, states.|
$1 billion  |44 |54 |MONEY| Monetary values, including unit.|

Here, the word Apple is the organization, the word UK is a geopolitical entity or country, and $1 billion is money. 

# Rule based NER to extract person names in Harry Potter book

## Data Source: 
* [Harry_Potter1-4/J. K. Rowling - Harry Potter 1 - Sorcerer's Stone](http://www.pauladaunt.com/books/Children's/Harry_Potter1-4/J.%20K.%20Rowling%20-%20Harry%20Potter%201%20-%20Sorcerer's%20Stone.txt)

* [List of Harry Potter characters](https://en.wikipedia.org/wiki/List_of_Harry_Potter_characters)

## How to Run locally?

1. Install `virtualenv` package.

    ```sh
    pip3 install virtualenv
    ```

2. Goto NER: Rule-based- SpaCy folder and open the terminal and type 

    ```sh
    virtualenv myproject
    ``` 
    to initialize the virtual environment on the project folder.


3. After this, you will need to activate the virtual environment to start working on the project through the terminal. Use the following command:

    ```sh
    source myproject/venv/bin/activate
    ``` 

    Once you do this, your prompt will change and it will show (myproject on the beginning of the absolute path of your project folder)

4. Install all required packages listed on requiremnts.txt

    ```sh
    pip3 install -r requirements.txt
    ``` 
    The project setup is complete now, let's run the project.

5. Create the spaCy Rule-based NER model by typing 
    ```sh
    python3 gen_model.py
    ``` 
    on the virtual environment activated terminal. The `gen_model.py` generates a rule-based spacy NER model. The model is then stored in path `model/hp_ner`. We will load this model to extract characters names in the Harry Potter book. 

6. To extract the names of characters in the book using the `hp_ner model` run:
    ```sh
    python3 main.py
    ``` 
    It will store character names on each chapter on `data/hap_data.json`


# Credits
* [Python Tutorials for Digital Humanities
](https://www.youtube.com/channel/UC5vr5PwcXiKX_-6NTteAlXw)

* [💥 Out now: spaCy v3.2 ](https://spacy.io/api/entityruler)