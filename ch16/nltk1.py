import nltk
nltk.download('book',quiet=True)
from nltk.book import *

print(nltk.corpus.gutenberg.fileids())
print('----------------------------------------------------------')
emma_raw = nltk.corpus.gutenberg.raw('austen-emma.txt')

#
print(emma_raw[:1302]) # 1302자 까지

