

a = [1,2,3]
b = a  # 주소복사

a[1] = 7
print(a, b)


b = a[:] # list(a) # 주소가 아닌 실제값을 복사
a[1] = 8
print(a,b)


