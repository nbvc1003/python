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

df = pd.read_csv('csv_exam1.csv', encoding='euc-kr')

plt.bar(df.index, df['국어'], color='r', label='국어')
plt.bar(df.index, df['영어'], color='g', label='영어', bottom=df['국어'])
plt.bar(df.index, df['수학'], color='b', label='수학', bottom=df['영어']+df['국어'])
plt.xticks(range(0,len(df.index),1), df['이름'])
plt.yticks(range(0,300,20)) # y축 범위
plt.title('학생별 성적표')
plt.legend()
plt.show()



