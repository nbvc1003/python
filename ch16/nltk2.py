import nltk
from nltk.tokenize import sent_tokenize, word_tokenize, RegexpTokenizer

emma_raw = nltk.corpus.gutenberg.raw("austen-emma.txt")

print(sent_tokenize(emma_raw[:1000])[3]) # ~1000 사이 3번째 문장
print(word_tokenize(emma_raw[50:100])) # 50~100 사이 단어들

rec = RegexpTokenizer("[\w]+") # [\w] (문자 or 숫자) 만 어러개(+).

print(rec.tokenize(emma_raw[50:100])) # 특수문자 제거 
