from nltk import Text
from konlpy.tag import *
from konlpy.corpus import kolaw
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

# pc에 설치된 폰트를 가져 와서 설정
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)
# 그래프에 - 표시를 보여준다.
plt.rcParams['axes.unicode_minus'] = False

okt = Okt()

c = kolaw.open('constitution.txt').read()


kolaw = Text(okt.nouns(c), name='kolaw') # 문서명을 kolaw로 지정

# 맣이 사용된 순서로 30개
kolaw.plot(30)
plt.show()