from scipy import stats
import pandas as pd


stock = {'다음' : [84900, 86100, 90800, 90600],
         '네이버' : [818000, 871000,796000, 806000],
        '넥슨' : [1756, 1836, 1720,  1713],
        'NC' : [292000, 295000,366500, 358500]
         }
df = pd.DataFrame(stock)
print(df)

slope, intersect, r_value, p_pvalue, stderr = stats.linregress(df['네이버'], df['넥슨'])
print('기울기: ', slope) #
print('절편: ', intersect) #
print('상관계수: ', r_value) # 1에 가까 울수록 관련이 높다.
print('유의수준: ', p_pvalue) #  < 0.05 -> 서로관계가 없다는 귀무가설을 기각
# 유의 수순 (p value) 0.05 보다 작을경우 귀무 가설 기각

# 기울기와 절편값을 이용해 다른쪽 가격을 유추할수 있다.
print('네이버 가격 900000 일때 넥슨 : ', 900000 * slope + intersect)