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

corrs = [1,0.7,0.3, 0, -0.3, -0.7, -1]
plt.figure(figsize=(len(corrs), 2)) # 그래프 캔버스 사이즈 (가로 len(corrs), 높이 2)

# index, value
for i,r in enumerate(corrs):

    # random.multivariate_normal() : 평균이 [0,0] 상관계수가 r인 데이터 1000건
    x, y = np.random.multivariate_normal([0,0], [[1,r],[r,1]], 1000).T
    # x, y = np.random.multivariate_normal([0, 0], [[1, r], [1, r]], 1000).T
    # print(x, y)
    # 1,7 에 1부터 7까지 순서대로 그린다.
    plt.subplot(1 , len(corrs), i+1)
    plt.plot(x,y, 'ro',ms=1)
    
    # x,y 가 동일한 길이를 갖도록
    plt.axis('equal')
    plt.title(r'$\rho$={}'.format(r)) # $\rho  = 상관계수 로 문자 표시

# plt.suptitle('상관계수와 스케너 플롯 보잉', y=1.1)
plt.show()




