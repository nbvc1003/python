import pandas as pd
import statsmodels.formula.api as sm

df = pd.read_csv('score.csv')

result = sm.ols(formula="score ~ iq + academy +game+ tv", data=df).fit()

print('계수:', result.params)
print('p_value :' , result.pvalues)
print('predicted values :' , result.predict())
print('결정계수 :' , result.rsquared) # 결정계수 = 상관계수 의 제곱

y = result.params.Intercept + (130 * result.params.iq) + (3 * result.params.academy) + \
    (2 * result.params.game) +(1 * result.params.tv)
print('예측점수는 : ', y)

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# 차트에 한글 가능하도록
from matplotlib import font_manager, rc, rcParams
font_name = font_manager.FontProperties(
    fname="c:/windows/Fonts/malgun.ttf").get_name()
rc('font',family=font_name)
rcParams['axes.unicode_minus'] = False # 부호표시 (-,+) 사용할때
###
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

import matplotlib.pyplot as plt

plt.plot(df['score'], label='실제성적')
plt.plot(result.predict(), label='예측성적')
plt.xticks(range(0,10,1), df['name']) # 인덱스에 해당하는 'name' 컬럼값으로 대치
plt.legend()
plt.show()