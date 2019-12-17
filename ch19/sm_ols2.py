import pandas as pd
import statsmodels.formula.api as sm


df = pd.read_csv('baseball.csv', encoding='euc-kr')
df = df[['타수','득점','2루타','3루타','홈런','삼진','타율']]

df['run'] = df['득점']/df['타수']
df['double'] = df['2루타']/df['타수']
df['tripple'] = df['3루타']/df['타수']
df['homerun'] = df['홈런']/df['타수']
df['strikeout'] = df['삼진']/df['타수']
df['avg'] = df['타율']
print(df)

result = sm.ols(formula='run ~ avg+strikeout+homerun+tripple+double', data=df).fit()
print('계수 :', result.params)

print('p_value:',result.pvalues)
print('predict :',result.predict())
print('Rsquaured :',result.rsquared)