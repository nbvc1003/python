from scipy import stats, polyval
import pandas as pd
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

stock = {'다음' : [84900, 86100, 90800, 90600],
         '네이버' : [818000, 871000,796000, 806000],
        '넥슨' : [1756, 1836, 1720,  1713],
        'NC' : [292000, 295000,366500, 358500]
         }
df = pd.DataFrame(stock)

print(stats.linregress(df['넥슨'], df['네이버']).rvalue)

slope, intersect, r_value, p_value, stderr = stats.linregress(df['네이버'], df['넥슨'])

# 네이버 값이 변할때 slop, intersect 를 가진 회귀값 -> 넥슨
ry = polyval([slope, intersect], df['네이버'])

plt.plot(df['네이버'],df['넥슨'], 'k.') # 좌표를 검정색 점으로
plt.plot(df['네이버'],ry, 'r')
plt.legend(['원데이터','회귀직선'])
plt.show()




