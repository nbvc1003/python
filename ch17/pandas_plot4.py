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

# species 컬럼을 기준으로 다시 만들고 value값은 mean()으로
df2 = iris.groupby(iris.species).mean()

# 컬럼 전체의 통칭 ( 범례의 title)
df2.columns.name = 'feature'

df2.plot.bar(rot=0) # rot= 0 -> x축 라벨의 모양
plt.title('feature별 평균')
plt.ylabel('종')
plt.show()
