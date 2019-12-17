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

titanic = sns.load_dataset('titanic')
df = titanic.pclass.value_counts() # pclass 컬럼의 빈도수를 구한다.

df.plot.pie(autopct="%.2f%%")
# plt.axis('equal') # 기준축 설정 
plt.axis('scaled')
plt.show()