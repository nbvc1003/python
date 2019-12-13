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


df = pd.read_csv('lovefruits.csv', encoding='euc-kr')
# print(df)
# 컬럼의 데이터 빈도수 sort : 정렬여부
data = df['선호과일'].value_counts(sort=True)
# data ->  index 가 과일명, 데이터가 빈도수 가되는 테이블 생성
# print(data)
plt.bar(range(0, len(data), 1), data, align='center')
# x축에 좌표 눈금명
plt.xticks(range(len(data)), data.index)
plt.title('과일 선호도')
plt.xlabel('과일명')
plt.ylabel('갯수')
plt.show()
