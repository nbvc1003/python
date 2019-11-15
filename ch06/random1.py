import random

# 0~1사이의 무작위 실수
print(random.random())

print(random.randint(1,45))

data = [1,2,3,4,5,6]
random.shuffle(data) # 랜덤셔플..ㄴ
print(data)