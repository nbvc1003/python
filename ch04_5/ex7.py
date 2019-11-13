


id = input('id :')
password = input("pass :")

if id == 'root' and password == 'system':
    result = '로그인 성공 '
elif password != 'system':
    result = '비밀번호가 틀렸습니다.'
else:
    result = '없는 아이디'

print(result)

w = int (input('수박 무게 :'))

if w > 10 :
    result = '1등급'
elif w > 7:
    result = '2등급'
elif w > 5:
    result = '3등급'
else:
    result = '4등급'

print(result)
    
    
    

