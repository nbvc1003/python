import re

# a[.]{3,}b


# acccb
# a....b
# aaab
# a.cccb


# p = re.compile("a[.]{3,}b") #  a와 b사이  . 3자이상
p = re.compile("a.{3,}") # \n을 제외하고 아우글자나 3자 이상
print(p.match("acccb"))
print(p.match("a....b"))
print(p.match("aaab"))
print(p.match("a.cccb"))
