import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# 한글 입력 가능하도록
from matplotlib import font_manager, rc, rcParams
font_name = font_manager.FontProperties(
    fname="c:/windows/Fonts/malgun.ttf").get_name()
rc('font',family=font_name)
rcParams['axes.unicode_minus'] = False # -표시 보이게
###
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

df = pd.read_csv('csv_exam1.csv',encoding='euc=kr')
# print(df)
# width 그림의 폭, df.index x축에서 그래프 시작 위치
plt.bar(df.index, df['국어'], width=0.3, color='r', label='국어')
plt.bar(df.index + 0.3 , df['영어'], width=0.3, color='g', label='영어')
plt.bar(df.index + 0.6 , df['수학'], width=0.3, color='b', label='수학')
plt.xticks(range(0, len(df.index),1), df['이름'], fontsize= 10)
plt.title('학생별 성적표')
plt.legend()
plt.show()


