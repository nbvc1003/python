file1 = open('test2.txt','r', encoding='utf-8')

for line in file1:
    print(line, end='')
file1.close()

print('------------------------------------------------')

file2 = open('test2.txt','r',encoding='utf-8')

content = file2.read() # 하나의 문자열로 변환

print(content)

file2.close()
print('===========================')

file3 = open('test2.txt','r',encoding='utf-8')
lines = file3.readlines() # list 형식으로 변환
print(lines)
file3.close()

