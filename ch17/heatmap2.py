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

tip = sns.load_dataset('tips')

# index day, colums sex
# heatmap color green

tip_data = tip.pivot_table(index=['day'], columns=['sex'], aggfunc='size')
print(tip_data)
#  as_cmap=True : 영역 구분 명확하게
sns.heatmap(tip_data, cmap=sns.light_palette('green', as_cmap=True))
plt.title('요일별 팁')
plt.show()
