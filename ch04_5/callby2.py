

# x = 20, y = 10
# call 함수에서 x,y를 받아서 x += y 를 실행한후에
# 함수 안에서 x,y출력, 함수 밖에서 x,y를 출력하고 비교

x= 20; y = 10
def call(x,y):
    x += y
    print('x : ', x,' , y:', y)

call(x,y)
print('x : ', x,' , y:', y)


# k = [1,2,3]
# k 에 4를 추가 하고 함수 안과 밖에서 출력
k = [1,2,3]

def call2(a):
    a.append(4)
    print('a :' , a)
call2(k)
print('k:',k)



