import pandas as pd

def cha(ar):
    return ar.max() - ar.min()

df = pd.read_csv('tips.csv')

result = df.groupby('sex')

# 기본 함수의 이름의 문자열로 넣으면 자동으로 적용된다.
# count, sum, min, max, mean 등등 가능
# 별도로 함수를 만들어서 사용가능
print(result['tip'].agg(['sum','mean',cha]))

