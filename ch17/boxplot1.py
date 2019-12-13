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

df = pd.read_csv('csv_exam1.csv', encoding='euc-kr')
# 값의 분포를 한눈에 알아 볼수 있도록
# 최대 최소 및 평균과 집중 분포 영역등 정보 전달.
plt.boxplot((df['국어'],df['영어'],df['수학']), labels=('국어','영어','수학'))
print(df['수학'].max())
print(df['수학'].min())
print(df['수학'].median())
print(df['수학'].mean())
plt.title('점수분포')
plt.show()