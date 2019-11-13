# 주사위 2개를 던져서 나온 숫자의 합이 6이되는 경우 출력

for i in range(1,7):
    for j in range(1,7):
        if i+j == 6:
            print('{} + {} = {}'.format(i,j,i+j))