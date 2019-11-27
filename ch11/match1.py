import re

match1 = re.match('[0-9]','1234') # 0~9사이의 숫자중에 '1234'의 문자열에 매치되는 값을 리턴
print(match1.group())

match1 = re.match('[0-9]','abc')
print(match1)


match1 = re.match('[0-9]+','1234') # 0~9사이의 숫자중에 '1234'의 문자열에 매치되는 값을 리턴
print(match1) # + 를 쓸경우 1개이상의 값
print(match1.group())

