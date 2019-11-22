def f(y):
    while True:
        print("숫자를 입력하세요")
        x = input()
        if x == 'x':
            break
        try: # 예외상황 캐치
            print(int(x) ** y)
        except:
            print("숫자가 아닙니다.")

f(3)