import numpy as np

x = np.array([18, 5, 10, 23, 19, -8, 10, 0, 0, 5, 2, 15, 8,
 2, 5, 4, 15, -1, 4, -7, -24, 7, 9, -6, 23, -13])

print('갯수 :',len(x))
print('함계 :', np.sum(x))
print('평균 :', np.mean(x), np.average(x))
print('분산 : ', np.var(x))
print('표준편차 :',np.std(x))
print('최대값:', np.max(x))
print('최소값:', np.min(x))
print('중앙값:', np.median(x))







