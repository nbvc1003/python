import json
import pandas as pd


obj = {"name":"철수", "addr":"서울",
       "친척":[{"name":"길동","age":22},{"name":"갑수", "age":35}]}
file = json.dumps(obj) # 파이썬 의 문자열로 변경

# file = '{"name": "\ucca0\uc218", "addr": "\uc11c\uc6b8", "\uce5c\ucc99": [{"name": "\uae38\ub3d9", "age": 22}, {"name": "\uac11\uc218", "age": 35}]}'

result = json.loads(file) # json data 해석
print(result)

siblings = pd.DataFrame(result["친척"],columns=['name','age'])
print(siblings)

df = pd.DataFrame(result)
print(df)

#             행 , 열
print(df.iloc[0,:2]) # [행, 열]
print(df.iloc[[0],[0,1]]) # [행, 열]

