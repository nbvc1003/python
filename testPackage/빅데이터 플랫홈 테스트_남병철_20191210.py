
# 2-1
text = open('test.txt','r',encoding='utf-8')
content = text.read()
print(content)
text.close()
# 2-2
text = open('test.txt','r',encoding='utf-8')
for line in text:
    print(line, end="")
text.close()

# 2-3
text = open('test.txt','r',encoding='utf-8')
textList = text.readlines()
print(textList, type(textList))
text.close()



# 7-1

def calculate_change(payment, cost):
    changeTotal = payment - cost
    unit = [50000,10000,5000, 1000]
    for i in range(len(unit)):
        print('{}원 지폐: {}장'.format(unit[i], changeTotal//unit[i]))
        changeTotal = changeTotal % unit[i]

calculate_change(100000, 33000)

