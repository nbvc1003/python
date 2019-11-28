import re

# 부정형 전방 탐색문 xxx를 제외시키고 탐색후 조회한다.

st = "foo.bar,autoexec.bat,sendmail.cf,a.exe"
# \n을 제외한 어떤 문자라도 여러번 반복 + 점(.) 확장자가 bat로 끝나지 않는
# \n을 제외한 여러문자
# p = re.compile('.*[.](?!bat$).*$')
p = re.compile('.*[.](?!bat$|exe$).*$') # exe 확장자도 제외

for i in st.split(","):
    m = p.search(i)
    if m != None:
        print(m.group())

# m = p.search(st)
# print(m.group())
