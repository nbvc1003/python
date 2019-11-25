# 대박 -> 쪽박
# 점심 -> 아침
# long -> short

f = open('test.txt', 'r',encoding='utf-8')

test = f.read()
f.close()

# 강력한 함수....
test = test.replace('대박', '쪽박')
test = test.replace('점심', '아침')
test = test.replace('short', 'long')

f = open('test.txt','w',encoding='utf-8')
f.write(test)

f.close()


