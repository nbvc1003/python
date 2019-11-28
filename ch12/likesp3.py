import numpy as np
arr = np.array([
        [[0,1],[2,3],[4,5]],
        [[6,7],[8,9],[10,11]]
    ])

# flatten , ravel 다차원 배열을 일차원 배열로 변환
print(arr, arr.shape)
print(arr.flatten())
print(arr.ravel())

