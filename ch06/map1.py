
def f1(x):
    return x*x

list1 = [1, 2, 3, 4, 5]
list2 = []
# print(f1(list))
for i in list1:
    list2.append(f1(i))

#print(list2)

# list1 안의 요소들을 함수 f1안에 대입하여 처리
# map  : 함수와 컬랙션을 받아서 매게 변수로 리턴

result = list(map(f1, list1))
print(result)

# f1을 람다로
result2 = list(map(lambda x: x*x, list1))
print(result2)