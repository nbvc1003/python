import numpy as np

ar = np.array([90, 40, 30, 78])

br = np.argsort(ar)  # 값의 크기순서를 rank값을 매겨서 출력
print(br)
print(ar[br]) # 내림차순으로
print(np.sort(ar)) # 동일


cr = np.argsort(-ar) # 값의 작은순서로 rank값을 매겨서 출력
print(cr)
print(ar[cr]) # 오름차순으로

print(np.sort(ar)[::-1]) # 위와 동일하게 오름차순 정렬