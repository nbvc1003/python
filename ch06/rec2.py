

def rec_f(num):
    if num > 0:
        print(num)
        rec_f(num-1)
    else:
        print("끝")


rec_f(5)

