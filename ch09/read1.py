

chichen1 = open('chicken.txt', 'r', encoding='utf-8')
for line in chichen1:
    print(line, end="")
chichen1.close() # 메모리에서 제거


