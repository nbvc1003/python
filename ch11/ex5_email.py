import re

email = "pahkey@gmail.com,Kim@daum.net,lee@myhome.co.kr"

p = re.compile(".*[@].*[.](?=com$|net$|co.kr$).*$")
for i in email.split(','):
    m = p.match(i)
    if m != None:
        print(m.group())