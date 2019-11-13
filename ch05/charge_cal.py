
# 거스름돈 계산기
# 50000, 10000, 5000, 1000
def calcurator_change(pay, price):
    change = pay - price
    moneys = [50000, 10000, 5000,1000]

    for i in moneys:
        print("{}원 {} 장".format(i, change //i))
        change %= i # 나머지 값을 저장후 다음 단계로 

calcurator_change(90000, 60000)

