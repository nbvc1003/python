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

# 21건의 랜덤한 정규분포 데이터 ( 가운데 몰려있는 평균0, 표준편차1)
x = np.random.normal(size=21)

bins = np.linspace(-4,4,17) # -4 ~ 4 : 17개
print(type(bins))
# 히스토그램 rug 실데이터, kde 밀도그래프
sns.distplot(x, rug=True, kde=True, bins=bins) # 분포를 보여주는 차트
plt.title('데이터 분포')
plt.show()

