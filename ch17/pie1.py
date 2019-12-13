import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# 차트에 한글 가능하도록
from matplotlib import font_manager, rc, rcParams
font_name = font_manager.FontProperties(
    fname="c:/windows/Fonts/malgun.ttf").get_name()
rc('font',family=font_name)
rcParams['axes.unicode_minus'] = False # 부호표시 (-,+) 사용할때
###
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

labels = ['개구리','돼지','개','통나무'] # 항목명
size = [15, 30, 45, 10] # 비율값
colors = ['yellowgreen','gold','lightskyblue','lightcoral'] # 각항목 컬러
explode = [0, 0.1, 0.5, 0] # 중심으로 부터 떨어진 거리
plt.title('원 그래프')
# autopct : 비율숫자표기 (%숫자.소수점f%% ), startangle : 시작지점 90도
plt.pie(size, explode=explode, labels= labels, colors=colors, autopct='%1.1f%%',
        shadow=True, startangle=90)
plt.axis('equal')
plt.show()