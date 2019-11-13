
week = input('요일을 첫자를 입력하세요')

if week == '월': result = 'monday'
elif week == '화': result ='Tuesday'
elif week == '수': result ='Wenesday'
elif week == '목': result ='Thuesday'
elif week == '금': result ='Friday'
elif week == '토': result ='Satureday'
elif week == '일': result ='Sunday'
else: result = '???'

print(result)