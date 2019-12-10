from nltk import Text
import matplotlib.pyplot as plt
import nltk
from nltk.tokenize import RegexpTokenizer

emma_raw = nltk.corpus.gutenberg.raw("austen-emma.txt")
retokenizer = RegexpTokenizer("[\w]+")

# name="Emma" : Emma라는 이름이 들어가는 문장
text = Text(retokenizer.tokenize(emma_raw), name="Emma") #

# dispersion_plot 단어가 사용된 위치를 시각화
text.dispersion_plot(['Emma','Knightley','Frank','Jane','Harriet','Robert'])

# Emma라는 단어가 사용된 위치를 직접 표시 문맥(앞뒤 단어)
text.concordance('Emma',10)
print('-----------------------------------------------------')
# Emma와 함께 문맥에서의 사용된 단어
text.similar('Emma',10)

plt.show()