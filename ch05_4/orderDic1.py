from collections import OrderedDict

keys = ['one','two','threee']
values = [1,2,3]

dic = dict(zip(keys, values))
print(dic)

# 추가된 순서를 기억해서 저장
dic2 = OrderedDict(zip(keys, values))

print(dic2)


for k in dic:
    print(k,':', dic[k])

for k in dic2:
    print(k,':', dic2[k])