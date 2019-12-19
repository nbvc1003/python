from scipy import stats
import scipy as sp

# binom 이항 분포 함수

# cdf 누적 분포 함수.
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.binom.html

# 승률 0.3 (30%) 의 확률에 100번시도시  60번 이상 이길 유의 확률(디폴트 유의수준 5% -> T검정)
print(1 - sp.stats.binom(100, 0.3).cdf(60 -1))
# 5.12994979828818e-10
# 60번이상 이길 확률은 극소
# 설명
## 0번 부터 59번까지 는 60% 라는 목적에 부함하지 않기 때문에 제외 시켜야 한다.
## 따라서 1 - sp.stats.binom(100, 0.3).cdf(60 -1) -> 나머지 60번 이상의 성공하는 케이스의 확률이 나온다.

# 위와 마찬가지로
#  승률 0.3 (30%) 100번시도시 30번 이상 이길 유의 확률(유의수순 5%)
print(1 - sp.stats.binom(100, 0.3).cdf(30 -1))
# 0.5376602639846385
# 거의 50% 이상

# 이후 T 검정을 실행
