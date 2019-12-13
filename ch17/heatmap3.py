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
import seaborn as sns

flights = sns.load_dataset('flights')

# 테이블 만들기  각 파라메타 -> x, y, value
flights_passengers = flights.pivot('month','year','passengers')
print(flights_passengers)
# fmt = 'd' : 정수만, annot=True : 숫자표시
sns.heatmap(flights_passengers,  annot=True, fmt="d", linewidths=1)
plt.show()