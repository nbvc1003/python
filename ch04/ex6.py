
def is_odd_even(num):
    if num%2 == 0:
        result = "짝수"
    else :
        result = "홀수"
    return  result;

print(is_odd_even(4))
print(is_odd_even(3))

def isEunYear(year):
    if year%400 == 0 or (year%4 == 0 and year %100 != 0):
        result = "윤년"
    else:
        result ="평년"
    return result

print(isEunYear(2000))
print(isEunYear(2100))








