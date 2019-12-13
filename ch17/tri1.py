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
#             x1,x2,x3
x = np.array([0,1,2])
#             y1, y2, y3
y = np.array([0,np.sqrt(3), 0])
triangles = [[0,1,2]]
tring = mtri.Triangulation(x,y, triangles)
plt.triplot(tring, 'ko-') # 검은색 포인트 o 실선
plt.xlim((-0.1,2.1)) # 시작부분 여분을 위해서 -0.1부터시작
plt.ylim(-0.1, 1.8)
plt.show()
