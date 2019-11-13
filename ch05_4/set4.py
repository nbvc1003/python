
a1 = {1,2,3,4,5}
a2 = {2,3,4}

print(a1.issubset(a2)) # a1 이 a2의 부분집합여부
print(a1.issuperset(a2)) # a1이 a2를 포함 하고 있는지 여부

if 3 in a1: # in은 데이터가 a1에 있는지 여부
    print("있어")
else: 
    print("없어")



