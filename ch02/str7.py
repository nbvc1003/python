
str ="c:\\data\\data.txt"

print(str.find("test"))
print(str.find("data"))

print(str.find('.'))

# 특정문자만 , 확장자 찾기
l1 = str.find('.')
print("확장자 : " + str[l1+1:])

s1 = str.split('.') # 배열로
print("확장자 : " + s1[1])
print("확장자 : " + s1[len(s1)-1])


