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

tips = sns.load_dataset('tips')

# 분포 현황을 대략적으로 파악 할수 있도록 표시
# 데이터가 겹치면 옆으로 출력 분산되어 보임
# sns.barplot(x='sex', y='tip', data=tips)
# sns.boxplot(x='sex', y='tip', data=tips)
sns.violinplot(x='day', y='total_bill', data=tips)
sns.swarmplot(x='day', y='total_bill', data=tips, color='green')

plt.show()