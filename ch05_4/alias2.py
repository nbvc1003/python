
# call by reference
# 대표적으로 배열, 함수객체
x = [2,3,5,7,11]
y = x  # 기존 리스트의 주소를 복사한다.
y[2] = 4

print(x)
print(y)

# 새로운 list를 만든다.
z = list(x)
z[2] = 3
print(x)
print(z)

