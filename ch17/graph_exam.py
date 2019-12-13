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

print(titanic)

sns.boxplot(x='class',y='survived', data=titanic, hue='sex')
# sns.barplot(x='class', y='survived', data=titanic, hue='sex')
# sns.swarmplot(x='class', y='survived', data=titanic, hue='sex')
# sns.violinplot(x='class', y='survived', data=titanic, hue='sex')
# sns.stripplot(x='class', y='survived', data=titanic, hue='sex', jitter=True)

plt.show()