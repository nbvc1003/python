import numpy as np

ar = [100,300,200]

# 파일 생성및 저장
np.save('ar', ar) # ar.npy로 저장
br = np.load('ar.npy')
print(br)

cr = ar + br
#확장자 npz
np.savez('dic',a=ar,b=br, c=cr) # dictionary 형식으로 저장
result = np.load('dic.npz')

print(result)
# key를 사용하여 출력
print(result['a'])
print(result['b'])
print(result['c'])

np.savetxt('test.csv',ar) # txt 형식으로 저장
cr = np.loadtxt('test.csv', delimiter=',') # , 로 구분해서 로드 .
print(cr)

