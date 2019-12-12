# x축 math = 77, 88, 99, 68
# y축 eng = 87, 96, 77, 65
# marker = o, 선 style = --, 선두께 5,
# title = 'style example'
# 마커 크기 = 15 ms(markersize)
# 마커 내부 색 g mfc(markerfacecolor)
# 마커 선 색 r mec(markeredgecolor)


import matplotlib.pyplot as plt
math = [77,88,99,68]
eng = [87, 96, 77, 65]
plt.plot(math,eng, marker='o', ls='--', lw=5, ms=15, mfc='g',mec='r',c='b')
plt.title('score')
plt.xlabel('math')
plt.ylabel('eng')
plt.show()




