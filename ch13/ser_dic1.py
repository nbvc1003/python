import pandas as pd

s = pd.Series([9904312, 3448737, 2890451, 2466052],
              index=['서울','부산','인천','대구'])
print('서울' in s, '대전' not in s)
print('서울' not in s, '대전' in s)

# 딕셔너리 성격과 유사..
for k, v in s.items():
    print(k, ' =',v)
print('---------------------------------------------------------')
# dictionary 만들었을경우는 인덱스 순서는 보장 안됨..
s2 = pd.Series({'서울':9904312, '부산':3448737, '인천':2890451,'대구':2466052})

print(s2)

