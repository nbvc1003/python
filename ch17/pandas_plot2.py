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
# rot : 회전각도
iris.sepal_length[:20].plot(kind='bar',rot=0)
plt.title("꽃 밭침 길이")
plt.xlabel('Data')
plt.ylabel('꽃 밭침 길이')
plt.show()
