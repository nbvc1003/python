

import math

# 표준편차 값 구하는 함수 
# 표준편차 ->  (값 -평균)^2 의 합 의 제곱근 == 분산의 제곱근
def stddev(*x):
    def mean():
        return sum(x)/len(x)
    #분산
    def variance(m):
        total = 0
        for arg in x:
            total += (arg - m) ** 2
        return total / (len(x) - 1)
    v = variance(mean())
    return math.sqrt(v)

print(stddev(2.3,1.7,1.4,0.7,1.9))
