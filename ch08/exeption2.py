


while True:


    snum1 = input("num1 :")
    snum2 = input("num2 :")

    if snum1 == 'x' or snum2 == 'x':
        print("종료")
        break;

    try:
        num1 = int(snum1)
        num2 = int(snum2)

        print("{}+{}={}".format(num1, num2, num1+num2))
        print("{}-{}={}".format(num1, num2, num1 - num2))
        print("{}*{}={}".format(num1, num2, num1 * num2))
        print("{}/{}={}".format(num1, num2, num1 / num2))
    
    except ZeroDivisionError:
        print("0으로 나눌수 없습니다.")
    except ValueError:
        print("숫자가 아닙니다.")
    finally:
        print("finally")