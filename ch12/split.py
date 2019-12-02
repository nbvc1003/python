import numpy as np
ar = np.arange(1, 17).reshape(4,4)
print(ar)
print("-------------------------------------------")
split1 = np.split(ar, 2, axis=0) #  axis=0 행기준  2개로
print(split1[0])
print(split1[1])

print("-------------------------------------------")
split1 = np.split(ar, [2,3], axis=0) #  axis=0 행 기준으로2행기준 3개로
print(split1[0]) # 2행 앞까지
print(split1[1]) # 2행 부터 3행 앞까지
print(split1[2]) # 나머지
print("-------------------------------------------")
# 0 :상하, 1: 좌우우
split1 = np.split(ar, 2, axis=1) # 열기준  2개
print(split1[0])
print(split1[1])
print("-------------------------------------------")
split1 = np.split(ar, [2,3], axis=1) #
print(split1[0]) # 2열 앞까지
print(split1[1]) # 2열 부터 3열 앞까지
print(split1[2]) # 나머지
