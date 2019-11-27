import re
print('주민번호 입력 ')

while True:
    no = input()
    if no == 'q': break
    p = re.compile('\d{6}-\d{7}')
    if p.search(no) != None:
        print('주민번호 입니다.')
    else:
        print('주민번호가 아닙니다.')



