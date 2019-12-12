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
# bar horizontal
plt.barh(df.index, df['국어'], color='r', label='국어')
# - 를 붙인다. (반대방향)
plt.barh(df.index, -df['영어'], color='g',label='영어')
plt.title('국어/영어 성적 비교')
# 세로로 그리기 때문에 y축에 이름을 넣는다.
plt.yticks(range(0, len(df.index), 1), df['이름'])
# 영어 점수가 음수 이므로 x 축에서 양수 처럼 보이도록
# plt.xticks([-100, -50, 0, 50,100], (100, 50,0, 50,100))
plt.xticks([-100, -50, 0, 50,100], [100, 50,0, 50,100])
plt.legend()
plt.show()