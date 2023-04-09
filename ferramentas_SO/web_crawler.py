'''
- é uma ferramente usada para encontrar, ler e indexir paginas de um site. 
- um robo que captura informações do que é mais relevante. 
- muito utilizado em processo de Pentest. 
'''
import requests
from bs4 import BeautifulSoup
import operator
from collections import Counter

def start(url):
    wordlist = []
    source_code = requests.get(url).text
    soup = BeautifulSoup(source_code, 'html.parser')
    for each_text in soup.find_all('div', {'class': 'entry-content'}):
        content = each_text.text
        words = content.lower().split()
        for each_word in words:
            wordlist.append(each_word)
        clean_wordlist(wordlist)


def clean_wordlist(wordlist):
    clean_list = []
    for word in wordlist:
        symbols = '!@#$%^&*()_-+={[]}|\;:?/>.<,"´`~'
        for i in range(0, len(symbols)):
            word = word.replace(symbols[i])
        if len(word) > 0:
            clean_list.append(word)
    create_dictionary(clean_list)


def create_dictionary(clean_list):
    word_count = {}
    for word in clean_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    for key, value in sorted(word_count.items(), key = operator.itemgetter(1)):
        print("% s : % s " % (key, value))
    c = Counter(word_count)
    top = c.most_common(10)
    print(top)


if __name__ == '__main__':
    start("https://pas.ava.ifsuldeminas.edu.br/")



    
