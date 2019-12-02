import re


# match : 데이터를 앞에서 부터 하나씩 조건에 맞는지 채크한다.

match1 = re.match('[0-9]',' 1234') # match의 경우 첫번째 데이터 부터 확인
print(match1) # 매치결과 값
print('-----------------------------------------------------------')
match1 = re.match('\s[0-9]',' 1234') # 첫글자는 공백이고 두번째 글짜가 숫자인지 확인
print(match1)
print('-----------------------------------------------------------')

match1 = re.search('[0-9]',' 1234') # search의 경우 전체 데이터 채크
print(match1)
print('-----------------------------------------------------------')

match1 = re.search('[0-9]+',' 1234') # search의 경우 전체 데이터 채크
print(match1) # + 를 쓸경우 조건에 맞는 요소들을 전부 
print('-----------------------------------------------------------')
