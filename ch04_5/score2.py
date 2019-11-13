
# 접수를 받아서 90보다 크면 A
# 80 :B, 70:c, 60, D, f

def score(num):
    if num > 90:
        result = 'A'
    elif num > 80:
        result = 'B'
    elif num > 70:
        result = 'C'
    elif num > 60:
        result = 'D'
    else:
        result = 'F'
    return  result;

while True:
    print(score(int(input('점수 : '))))


