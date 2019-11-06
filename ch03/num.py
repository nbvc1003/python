
num =[3,5,6,7]

# 문자열은 특정index 값을 변경하지 못하지만 list는 가능 
num[1] = 12
num[0] = num[2] + num[3]
print(num)