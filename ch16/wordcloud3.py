from wordcloud import WordCloud
import matplotlib.pyplot as plt
from konlpy.corpus import kobill
from konlpy.tag import Okt
from collections import Counter
import pytagcloud
import nltk


font_path = "c:/Windows/Fonts/malgun.ttf"

print(kobill.fileids())

text = kobill.open('1809899.txt').read() # 300자 까지
# print(text)

okt = Okt()

nouns = okt.nouns(text)

for noun in nouns:
    if len(noun) < 2:
        nouns.remove(noun)

# count = Counter(nouns)
text1 = nltk.Text(nouns)

data1 = text1.vocab()

data300 = data1.most_common(300)
dic = dict(data300)
wc = WordCloud(width=1000, height=600, background_color='white', font_path=font_path)

plt.imshow(wc.generate_from_frequencies(dic))
plt.axis('off')
plt.show()