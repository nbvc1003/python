import numpy as np
import matplotlib.pyplot as plt

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# 한글 입력 가능하도록
from matplotlib import font_manager, rc, rcParams
font_name = font_manager.FontProperties(
    fname="c:/windows/Fonts/malgun.ttf").get_name()
rc('font',family=font_name)
rcParams['axes.unicode_minus'] = False # -표시 보이게
###
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# 평균이 0 , 표준편차 1, 갯수가 100
x = np.random.normal(0,1, 100)
y = np.random.normal(0,1, 100)
plt.title('산포도 그래프')

plt.scatter(x,y)
plt.show()