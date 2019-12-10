import pandas as pd

def func(s):
    if len(s) < 5: return s
    else: return s[0:3]+'...'

loc = {'한국':'korea','중국':'china','일본':'japan'}
df = pd.DataFrame([['안녕하세요','니하오','곤니치와','안녕하세요'],
                   ['한국','중국','일본','한국']]).T
print(df)
print('===========================================================')
df.columns = ['인사말','국가']
print(df)
print('===========================================================')
# drop_duplicates : 중복된 데이터 삭제
df = df.drop_duplicates()
print(df)
print('===========================================================')
# map : dict 또는 함수를 수행한 결과
# nation 컬럼을 생성하고 df[국가] 컬럼의 데잍터를 loc 와 매칭시켜 결과 데이터를 생성된 컬럼의 값으로 넣는다.
df['nation'] = df['국가'].map(loc)
print(df)
print('===========================================================')
# 인사말 컬럼의 내용을 func 함수 를 적용하여 바꿔준다.
df['인사말'] = df['인사말'].map(func)
print(df)