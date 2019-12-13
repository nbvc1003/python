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

# x축과 y축의 컬럼을 지정 data = dataframe 형식의 데이터
print(iris)

# histogram과 scatter를 함께 표현
sns.jointplot(x='sepal_length', y='sepal_width', data=iris, kind='scatter')
plt.title("붓꽃의 꽃받침의 길이/폭")
plt.show()
