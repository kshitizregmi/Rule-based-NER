import wget
def download(url):
    filename = wget.download(url, out='data/')

url1 = 'https://raw.githubusercontent.com/wjbmattingly/ner_youtube/main/data/hp.txt'
url2 = 'https://raw.githubusercontent.com/wjbmattingly/ner_youtube/main/data/hp_characters.json'


download(url1)
download(url2)