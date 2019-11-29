import numpy as np

# ar 21~40 5행 4열
br1 = np.array(['A','B','C','A','C'])
ar = np.arange(21,41).reshape(5,4)
print(ar)
# br1이 A 아닌경우 출력
# 위 조건에서 3열 출력
# 위 조건에서 2열 부터 끝까지 술력
# 위 조건 데이터만 67로 변경하고 출력

print(br1!='A')
print(ar[br1!='A',3])

print(ar[br1!='A',2:])
ar[br1!='A',2:] = 67
print(ar)


print(ar[(br1=='A')|(br1=='C')])