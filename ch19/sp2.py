from scipy import stats
import scipy as sp


# binom 확률 질량 함수
# cdf 누적 분포 함수.
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.binom.html

# 이항확률분포가 확률이 0.3 시도 횟수가 100번일때 60번을 성공할 확률
print(sp.stats.binom(100, 0.3).pmf(60)) # 60번 성공 확률
# 이항확률분포가 확률이 0.3 시도 횟수가 100번일때 60번까지 누적된 확률
print(sp.stats.binom(100, 0.3).cdf(60)) # 60번 까지 누적된 확률 max 1 (누적이기 때문에 x값이 커질수록 값은 1에 가까워진다.)



# 시도 횟수 , 성공 확률, cdf (예상 성공수) -> 확률
print(sp.stats.binom(100, 0.3).cdf(60)) # 60번 성공 확률
print(sp.stats.binom(100, 0.3).cdf(30)) # 30번 성공 확률

print(sp.stats.binom(100, 0.5).cdf(50))

# 100번시도시 승률 0.3 (30%) 일때 60번 이길 유의 확률(디폴트 유의수준 5%)
# 아래 값이 0.05 보다 작은지 여부를 확인한다.
print('1:', 1 - sp.stats.binom(100, 0.3).cdf(60 -1))
# 100번시도시 승률 0.3 (30%) 일때 30번 이길 유의 확률(유의수순 5%)
print(1 - sp.stats.binom(100, 0.3).cdf(30 -1))

