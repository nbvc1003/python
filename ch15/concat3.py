import pandas as pd

stock1 = {
'2017-03-20': [84900, 818000, 1756,292000],
'2017-03-21': [86100, 871000, 1776,295000]}
stock2 = {
'2017-04-20': [90800, 796000, 1695],
'2017-04-21': [90600, 806000, 1703]}

df1 = pd.DataFrame(stock1, columns=['2017-03-20', '2017-03-21'],
                   index=['다음','네이버','넥슨','NC'])
df2 = pd.DataFrame(stock2, columns=['2017-04-20','2017-0421'],
                   index=['다음','네이버','넥슨'])

print(pd.concat([df1, df2], axis=1, sort=True))
print(pd.concat([df1, df2], axis=1, sort=True).fillna('-')) # NaN 대신 - 로
print(pd.concat([df1, df2], axis=1, sort=True, join='inner'))


