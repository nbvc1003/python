



num=[2,3,4,5]

# 인덱스를 가져 오는 방법
for i in range(len(num)):
    print(num[i])

# 데이터 자체를 가져오는 방법
for i in num:
    print(i)

while num:
    print(num.pop())