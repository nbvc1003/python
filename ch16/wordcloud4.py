from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

# 한글 그래프 처리시 필수
from matplotlib import font_manager, rc
import re


font_path = "c:/Windows/Fonts/malgun.ttf"
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)
plt.rcParams['axes.unicode_minus'] = False

text = open('ab.txt','r',encoding='utf-8').read()
# print(type(text))
## 영문 숫자 제거 (한글만 가져 오는 방식)
text = re.compile('[가-힣]+').findall(text)
# print(type(text))
text = ' '.join(text)# list 를 string 으로 만들고 아이템 사이는 공백을 넣는다.
# print(type(text))

wordcloud = WordCloud(font_path= font_path).generate(text)


plt.imshow(wordcloud)
plt.axis("off")
plt.show()