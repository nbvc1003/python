
f = open('capital.txt', 'w', encoding='utf-8')
while True:
    nation = input('나라이름:')
    if nation == 'q': break
    capi = input('수도')
    f.write('{}:{}\n'.format(nation, capi))
print('생성완료')

f.close()






