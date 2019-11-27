import re


data = """
    park 010-1234-5678
    kim 010-1111-2222
    """

# 010-1234-**** park
# 010-1111-**** kim


p = re.compile('(\w+)\s(\d+[-]\d+)[-](\d+)')
print(p.sub("\g<2>-**** \g<1>",data))
print("===========================================")

for i in data.split("\n"):
    m = p.search(i)
    if m != None: # \n으로 잘랐을경우 공백 문자가 포함되어 None값이 나올수 있다.
        print(m.group(2) + "-****"+" "+m.group(1))
