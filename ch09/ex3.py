f = open('test.txt', 'r', encoding='utf-8')
lines = f.readlines()
print(lines)
f.close()

# 거꾸로 
lines.reverse()

f = open('test.txt', 'w', encoding='utf-8')

for line in lines:
    f.write(line)
f.close()
