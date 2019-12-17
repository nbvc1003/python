from scipy import stats
import scipy as sp


# binom 확률 질량 함수
# cdf 누적 분포 함수.
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.binom.html


# 시도 횟수 , 성공 확률, cdf (예상 성공수) -> 확률
print(sp.stats.binom(100, 0.3).cdf(60)) # 60번 성공 확률
print(sp.stats.binom(100, 0.3).cdf(30)) # 30번 성공 확률

print(sp.stats.binom(100, 0.5).cdf(50))

# 100번시도시 승률 0.3 (30%) 일때 60번 이길 유의 확률(디폴트 유의수준 5%)
print('1:', 1 - sp.stats.binom(100, 0.3).cdf(60 -1))
# 100번시도시 승률 0.3 (30%) 일때 30번 이길 유의 확률(유의수순 5%)
print(1 - sp.stats.binom(100, 0.3).cdf(30 -1))

