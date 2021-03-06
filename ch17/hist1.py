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
data = pd.concat([df['국어'], df['영어'],df['수학']])
print(data)
plt.hist(data, bins=3)
# 하 :0 ~ 40 , 중: 41 ~ 80, 상: 80 ~ 100
plt.xticks(range(0,100, 40),['하','중','상'])
plt.title('점수 빈도')
plt.show()
