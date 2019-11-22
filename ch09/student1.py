file = open('students.txt','r')

talls = []
wtotal = []
for line in file:

    lists = line.split(',')
    talls.append(int(lists[2].strip()))
    wtotal.append(int(lists[3].strip()))
print("키의 평균{}, 몸무게 평균{}".format(sum(talls)/len(talls), sum(wtotal)/len(wtotal)))
file.close()