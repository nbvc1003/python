family = {}
family['어머니'] = 'grace'
family['아버지'] = 'chris'
family['아들'] = 'young'
family['딸'] = 'kay'

# xxx는 누구 입니까?
# 데이터를 받아서

for i in family.keys():
    ans = input('{}는 누구 ? :'.format(family[i]))
    if ans == i:
        print('정답입니다. ')
    else:
        print('오답입니다. 답은 {} '.format(i))



