


def sum_digits_old(sum, n):
    s = str(n)

    if len(s) < 2:
        sum += int(s)
    else:
        sum = int(s[0]) + sum_digits_old(sum, int(s[1:]))

    return sum



# 추천
def sum_digits(n):
    if n < 10:
        return n
    else:
        str_n = str(n)
    return int(str_n[0]) + sum_digits(int(str_n[1:]))

print(sum_digits_old(0,1346))
print(sum_digits(1346))
