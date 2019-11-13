
t1 = ()

t2 = (1,)  # tuple 타입임을 인식 시키기위해서 , 를 넣어줌
t3 = (1)  # tuple 타입이 아닌 int 형으로 인식

t4 = (1, 2, 3)
t5 = 1, 2, 3  # ( ) 가 없어도 tuple로인식
t6 = ('a', 'b', ('ab', 'bc'))  # 중첩 tuple 가능

print(type(t1))
print(t2, type(t2))

print(t3, type(t3))
print(t4, type(t4))
print(t5, type(t5))
print(t6, type(t6))
