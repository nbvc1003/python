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

import scipy as sp

mu = 0
std = 1
rv = sp.stats.norm(mu, std) # 조건의 정규분포 데이터
print(type(rv))
xx = np.linspace(-4, 5, 100) # ~4 ~ 5 중 0, 1 인 값 100개
x = rv.rvs(100) # 정규분포 데이터 100건추출
print(x)


# rv.pdf 확률밀도 함수
plt.plot(xx, rv.pdf(xx))
plt.title("정규분포 곡선")
plt.show()