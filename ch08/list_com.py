
# List Comprehention
li = [n for n in range(11)]
print(li)


li2 = [n*n for n in range(11)]
print(li2)

# 아래와 같은 코드를 위와 같이 간단하게 줄여 준다.
li3 = []
for i in range(11):
    li3.append(i*i)
print(li3)

