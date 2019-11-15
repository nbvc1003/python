

from functools import reduce

print(reduce(lambda x,y:x+y, [47,11,42,13]))

x = [47,11,42,102,13]
f = lambda a,b : a if (a>b) else b

# 함수의 조건으로 인자값들을 계산해서 결과만 리턴..
print(reduce(f,x))
