


while True:
    str = input("몇단? :")
    if(str.isnumeric() == False):
        print("숫자아닙니다. ")
        continue
    num = int(str)
    if num != 0:
        i = 2
        while i <= 9:
            print("{} * {} = {}".format(num, i, num*i))
            i += 1
    else: break;
