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

# distplot : Histogram과 유사한 그래프 ..(빈도를 보여주기 위한 목적)
# distplot을 그릴때 kde(밀도), rug(실제데이터) 를 함께 그린다.
sns.distplot(x, kde=True, rug=True)


plt.title('꽃잎 길이 Dist plot')
plt.show()