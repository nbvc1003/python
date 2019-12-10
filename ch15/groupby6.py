import pandas as pd

def cha(ar):
    return ar.max() - ar.min()

df = pd.read_csv('tips.csv')

result = df.groupby('sex')

# 성별로 팁의 최대 최소 차이
print(result['tip'].aggregate(cha))

