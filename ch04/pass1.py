

# in,  not in

pocket = ['휴대폰','지갑', '종이']
if '지갑' in pocket :
    money = int(input("지갑에 돈이 얼마"))
    if money > 10000: print('택시타고가')
    else : pass
else :
    card = input('카드 있니 y/n 으로 ')
    if card == 'y':
        print('택시')
    else:
        print('걸어가')

