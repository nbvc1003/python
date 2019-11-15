


some_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def flip(some_list):
    str = []
    for i in range(len(some_list)):
        str.append(some_list[len(some_list)-1 - i])
    return str

def flip2(some_list):
    if len(some_list) < 2:
        return some_list
    else:
        return flip2(some_list[1:]) + some_list[:1]


# 3가지 방법 의 결과는 동일
print(flip(some_list))
print(flip2(some_list))
print(some_list[::-1])
