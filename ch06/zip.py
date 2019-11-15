

a1 = [90, 85, 95, 80, 90, 100, 85, 75, 85, 80]
a2 = [95, 90, 90, 90, 95, 100, 90, 80, 95, 90]

# 값 2개를 tuple형식으로 묶어 준다.
a = list(zip(a1,a2))

print(a)
print(type(a))

for i , j in a:
    print(i+j)

