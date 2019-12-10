import pandas as pd

def descsort(df, column='time'):
    return df.sort_values(by=column, ascending=False)


df = pd.read_csv('tips.csv')

print(df.groupby('sex').apply(descsort)) # time 별로
### 유의사항
# .apply(func, param) : func에 필요한 인자는 별도 인자값으로 따로 넣어 준다.

print(df.groupby('sex').apply(descsort, column='total_bill')) # 팁 토탈 큰순
print(df.groupby('sex').apply(descsort, column='size')) # size가 많은 순..

