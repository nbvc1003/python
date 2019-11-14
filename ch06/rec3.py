


def facto1(num):
    if num > 1 :
        print(num,'*', end='')
        return facto1(num-1) * num
    else:
        print(' 1 = ', end='')
    return 1

# 5 * 4 * 3* 2 * 1 = 120
print(facto1(5))


def facto2(num):
    tot = 1
    for i in range(num):
        if i < num-1:
            print( num - i, '*', end='')
            tot *= (num-i)
        else :
            print(' 1 = ', end='')
    return tot

print(facto2(5))


