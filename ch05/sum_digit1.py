

# 자리수 숫자 의합
def sum_digit(num):
    num = str(num) #  문자열로 
    sum = 0
    for i in range(len(num)): # 문자열 길이만큼 
        sum += int(num[i]) # 각 문자열 인덱스의 값을 숫자로 & 합 
    return sum


print(sum_digit(486))


