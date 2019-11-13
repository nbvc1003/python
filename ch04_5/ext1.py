
a, *b = [1,2,3,4,5]

print(a) # a = 1 값만
print(b) # b 에 2,3,4,5 값이..

*a, b = [1,2,3,4,5]
print(a)
print(b)

a, *b, c = [1,2,3,4,5]
print(a)
print(b)
print(c)

a, b, *c = [1,2,3,4,5]
print(a)
print(b)
print(c)

# 아래와같은 경우 오류
# b와 c에 몇개씩의 별수가 대입될지 정해지지 않았다.
#a, *b, *c = [1,2,3,4,5]




