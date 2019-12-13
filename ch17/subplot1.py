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

fig, ax_lst = plt.subplots(2,2,figsize=(8,5))
#
ax_lst[0][0].plot([1,2,3,4], 'ro-') # 'ro-' : red 포인트는 o 모양 실선
ax_lst[0][1].plot(np.random.randn(4,10), np.random.randn(4,10), 'bo--') # 'ro--' red 포인트 o 긴점선
ax_lst[1][0].plot(np.linspace(0.0, 5.0),np.cos(2*np.pi*np.linspace(0.0,5.0))) # 코사인 라인
#                  x1,y1  x2, y2
ax_lst[1][1].plot([3, 5], [3, 5], 'bo:') # 두점사이 직선 파란색 포인트o 점선으로
plt.show()