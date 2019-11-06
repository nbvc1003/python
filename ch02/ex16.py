

# name(이름), nationality(국적), phone_number(핸드폰 번호)라는 변수를 만들고, 여러
# 분에게 알맞은 정보들을 지정하세요.
# 변수와 문자열 포맷팅을 이용하여 아래와 같이 출력되게 하세요.
# Hi, my name is kildong. I'm from Korea.
# My phone number is 010-1234-5678.
# name을 문자열 “kildong "으로, nationality를 문자열 "Korea"로, 그리고
# phone_number를 문자열 "010-1234-5678"로 지정

name = 'kildong'
nationality = 'korea'
phone_number = "010-1234-5678"

print("HI, myname is %s. I'm frome %s"%(name, nationality))
print("My phone number is {phone_number}".format(phone_number = phone_number))

