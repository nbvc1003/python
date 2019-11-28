import re


# 긍정형 전방 탐색은 xxx를 포함해서 검색후 출력에서 제외 시키는 방법

p = re.compile(".+:") # \n제외한 모든 문자(.) 를 여러번 사용하고 끝에 :
m = p.search("http://www.google.com")
print(m.group())
print ("=============================================")



#(?=...) 긍정형 전방 판정
# 조건을 검색할때는 사용하고 결과리턴에는 포함하지 않는 식
p = re.compile(".+(?=:)") # \n제외한 모든 문자(.) 를 여러번 사용하고 끝에 :
m = p.search("http://www.google.com")
print(m.group())


