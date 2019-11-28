import numpy as np

# random 함수의 값을 고정..
np.random.seed(seed=1234)

print(np.random.normal(size=5))
print(np.random.normal(size=(2,3)))

