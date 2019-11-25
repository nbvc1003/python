f = open('sample.txt')
sum = cnt = 0
for line in f:
    score = int(line)
    sum += score
    cnt += 1

print('합계 :', sum,",평균:", sum/cnt)

f.close()

with open('result.txt','w',encoding='utf-8') as f2:
    f2.write('합계 : {}\n'.format(sum))
    f2.write('평균 : {}\n'.format(sum/cnt))

