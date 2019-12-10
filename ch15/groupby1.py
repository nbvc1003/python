import pandas as pd

df = pd.read_csv('tips.csv')
print(df)
print('========================================================================')
# time 별로 묶인 tip의 데이터
gp = df['tip'].groupby(df['time'])
print(gp)
for name , group in gp:
    # name : tip , group : time
    print(name)
    print(group)


