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

iris = sns.load_dataset('iris')
x = iris.petal_length.values

# 단순 데이터들의 위치를 표시 한다.
sns.rugplot(x)

# 데이터의 밀도를 그래프로 표현한다.
sns.kdeplot(x)
plt.title('꽃 잎 길이에 대한 Kernal 밀도 그래프')
plt.show()