
# 거스름돈을 출력
# 파라메타의 값은 1000의 배수
# 50000, 10000, 5000, 1000

# 지불금, 가격
def calculate_change(payment, cost):

    if payment >= cost:
        changeTotal = payment - cost
        print('5만원 지폐 : {}장'.format(changeTotal // 50000))
        changeTotal = changeTotal % 50000
        print('1만원 지폐 : {}장'.format(changeTotal // 10000))
        changeTotal = changeTotal % 10000
        print('5천원 지폐 : {}장'.format(changeTotal // 5000))
        changeTotal = changeTotal % 5000
        print('1만원 지폐 : {}장'.format(changeTotal // 1000))
    else:
        print("금액이 부족 합니다. ")

def calculate_change2(payment, cost):
    changeTotal = payment - cost
    unit = [50000, 10000,5000,1000]
    for i in range(len(unit)):
        print('{}원 지폐: {}장'.format(unit[i], changeTotal//unit[i]))
        changeTotal = changeTotal % unit[i]

calculate_change(500000, 378000)

calculate_change2(500000, 378000)