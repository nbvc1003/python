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

# bar그래프 : 점수를 보여주는 목적
# histgram 그래프 : 해당점수가 몇명인가를 보여주기 위함 즉 빈도수에 중점
df = pd.read_csv('csv_exam1.csv', encoding='euc-kr')
plt.hist([df['국어'],df['영어'],df['수학']],bins=10,
         label=['국어','영어','수학'])
plt.title('점수 빈도')
plt.legend()
plt.show()