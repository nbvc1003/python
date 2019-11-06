


b = [1,2,['a','b',[7,8,9]]]

print(b[2][2][2])

a1 = [7,5,2,['a','b','c','d'],12,15]

print(a1[1], a1[2])
print(a1[3][2], a1[3][3])
print(a1[4], a1[5])

print(a1[3][0] + 'hi')

a2 = [1,2,'a']
print(a2[2] + 'hi')

a2[0] = 5
print(a2)
del a2[0]
print(a2)
