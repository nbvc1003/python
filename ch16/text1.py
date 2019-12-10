from nltk import Text

import matplotlib.pyplot as plt

import nltk

from nltk.tokenize import RegexpTokenizer

emma_raw = nltk.corpus.gutenberg.raw("austen-emma.txt")

#특수 문자를 제거 하고 순수한 숫자+문자
retokenize = RegexpTokenizer("[\w]+")
# 숫수문자만 단어별로 분리하여 텍스트형식으로
# 단어 갯수 count
text = Text(retokenize.tokenize(emma_raw))

# 많이 나오는 단어 순으로 20개 추출하여 그래프
text.plot(20)
plt.show()