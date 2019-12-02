import pandas as pd

s = pd.Series(range(3), index=['a','b','c'])
print(s)
# index가 문자인 경우 속성처럼 스리즈명.인덱스명 으로 사용가능 
print(s[1], s['b'],s.b) # 3가지 방법으로 사용가능

