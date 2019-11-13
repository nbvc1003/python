


# *변수 : 값이 여러개 넣을수 있다.
# **변수 : dictionary 데이터 ( 키:값 형식의 여러개 )
def f(height, weight, **k):
    print('키 :', height)
    print('몸무게 :', weight)
    print(k)

#
f(height=182, weight=89, age=27, name='강다니엘')

