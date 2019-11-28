import numpy as np

ar1 = np.array([1,2,3]) # 1차
ar2 = np.array([4,5,6]) # 1차

br = np.array([[6,7,8],[10,11,12]]) # 2차
print(ar1*2) # 각각의 항목마다 2를 곱한다.
print(ar1 + ar2) # 같은 위치 끼리 연산
print(ar1 - ar2) #

print(ar1 * ar2) # 같은 위치 끼리 곱한다.
print(ar1 / ar2) # 같은 위치 끼리 나눈다.

print(ar1 + br)
# 각 항에서 ar1을 br의 첫행과 연산
# ar1 을 2번째 행과 연산해서 2행

print(ar1 - br)
print(ar1 * br)
print(ar1 / br)







