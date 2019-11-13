

def person(height, weight):
    # 'd' 정수만 출력 하도록 강제 한다.
    print('키 : ', format(height, 'd'))
    print('몸무게 :', weight)
person(174, 70)
#person(174.3, 70) # 애러발생

# 파라메타의 순서와 상관없이 파라메터에 직접 값을 넣을수 있다.
person(weight=67, height=181)
