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
import matplotlib.tri as mtri

## 점들의 좌표
#           x:0,1,2,3,4,5
x = np.array([0,1,2,3,4,2])
#          y: 0, 1.xx        0,  1.xx  , 0,  2.xxx
y = np.array([0, np.sqrt(3),0,np.sqrt(3), 0,2*np.sqrt(3)])

# 각점들의 인덱스 3개씩을 묶어서 선으로 이어준다.
triaglues = [[0,1,2],[2,3,4],[1,2,3],[1,3,5]]

triang = mtri.Triangulation(x,y, triaglues) # 점x,y 값, 각점들의 묶음
plt.triplot(triang, 'ko-') # 그리함수 + 스타일지정
plt.xlim((-0.1, 4.1))
plt.ylim((-0.1, 3.7))
plt.show()