

# 팩토리얼 계산
# 5! = 5 * 4 * 3 * 2 * 1

def facto1(num):
    if num > 0 :
        return facto1(num-1) * num
    return 1

print(facto1(5))


def facto2(num):
    tot = 1
    for i in range(num):
        tot *= (num -i)

    return tot

print(facto2(5))