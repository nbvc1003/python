def sum(num):
    tot = 0
    for i in range(1, num+1):
        tot += i
    print("합계 :", tot)
sum(10)
sum(7)


def rec_sum(tot,num):
    if num  > 0 :
        tot += num
        rec_sum(tot, num - 1)
    else:
        print("합계 :", tot)


rec_sum(0, 10)
rec_sum(0, 7)