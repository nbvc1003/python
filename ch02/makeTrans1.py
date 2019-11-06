

instr = "abcdef"
outstr = "123456"
trans = ''.maketrans(instr, outstr)
str = "hello world"
# str 문자를 위 trans 규칙에 따라서 변경한다.
print(str.translate(trans))

instr1 = '0123456'
outstr1 = '영일이삼사오육'

trans1 = ''.maketrans(instr1,outstr1)
str = '67530'
print(str.translate(trans1))