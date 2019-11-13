

k1 = ['one','two','three']
v1 = (1,2,3)
d1 = dict(zip(k1, v1)) # zip을 사용하여 키,value 로 사용가능

print(d1)

for k in d1: # d1에서 키가 하나씩 k에 저장
    print(k, ':', d1[k])
    