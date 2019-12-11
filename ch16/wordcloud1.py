from wordcloud import WordCloud
import matplotlib.pyplot as plt
from konlpy.corpus import kolaw
from konlpy.tag import Okt
import nltk

# 한글 그래프 처리시 필수
from matplotlib import font_manager, rc
font_path = "c:/Windows/Fonts/malgun.ttf"
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)
plt.rcParams['axes.unicode_minus'] = False

data = kolaw.open('constitution.txt').read()
okt=Okt()
nouns=okt.nouns(data) # okt로 명사추출
text = nltk.Text(nouns) # 단어별로 나열된 text 형 문서 
# print('text',text)
data1 = text.vocab()
# print('data1',data1)
data500 = data1.most_common(500) # 가장 많이 사용되는 순서로 500

dic = dict(data500) # dictionary 형태로 단어:갯수
# print('dic',dic)

wc = WordCloud(width=1000, height=600, background_color='white', font_path=font_path)
plt.imshow(wc.generate_from_frequencies(dic))
plt.axis('on') # x/y 축 표시 여부
plt.show()


