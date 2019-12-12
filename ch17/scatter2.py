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

df = pd.read_csv('korea.csv', encoding='euc-kr') # ms949
# print(df)

plt.scatter(x=df.index, y=df['점수'], marker='2')
# 0~index 갯수 1씩증가하며 '이름' 값을 표시, 세로로 표시
plt.xticks(range(0,len(df['점수']),1),df['이름'], rotation='vertical') #
plt.title('학생 국어점 수 산포도')
plt.show()