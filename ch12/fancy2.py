import numpy as np

ar = np.arange(8).reshape(2,4)
print(ar)

print(ar[0,0]) # 0행 0열 
print(ar[1,1]) # 1행 1열
print(ar[-1,-1]) # 마지막행 마지막열

print(ar[0,:]) # 0행 모든 데이터
print(ar[:,0]) # 행은 전부 열은 0열 (0열 전부)

print(ar[:2, :2]) # 2행 앞전부, 2열앞 전부

ar2 = np.arange(10)

index = np.array([True,False,True,False,True,False,True,False,True,False])
print(ar2[index]) # True인 경우
print(ar2[ar2%3 == 0]) # 3의 배수

ar3 = np.arrange(4) *10 # 0 ~ 3 까지 배열에 각각 10을 곱하기

print(ar3) #

idx = np.array([0,0,0,0,1,1,1,1,2,2,2,2,3,3,3,3])
print(ar3[idx]) # 해당하는 인덱스 데이터 추출












