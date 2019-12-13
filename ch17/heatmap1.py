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

titanic_size = titanic.pivot_table(index='class', columns=['sex'], aggfunc='size')

print(titanic_size)
#  as_cmap=True : 영역 구분 명확하게
sns.heatmap(titanic_size, cmap=sns.light_palette('red', as_cmap=True),
            annot=True, fmt='d')
plt.title('타이타닉 층별 성별 승객수')
plt.show()
