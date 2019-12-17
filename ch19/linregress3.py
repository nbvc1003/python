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

slope, intersect, r_value, p_value, stderr = stats.linregress(df['다음'], df['NC'])

print('기울기 :',slope)
print('절편  :',intersect)
print('상관계수  :',r_value)
print('유의수준  :',p_value) # 높으면 귀무가설 채택 ( 귀무가설 두 사건이 관련이 없다, 연관성이 없다)

# 다음 값이 변할때 slop, intersect 를 가진 회귀값 -> NC
ry = polyval([slope, intersect], df['다음']) # (p, x)

plt.plot(df['다음'],df['NC'], 'k.') # 좌표를 검정색 점으로
plt.plot(df['다음'],ry, 'r')
plt.title('다음과 NC 의 관계')
plt.legend(['원데이터','회귀직선'])
plt.show()