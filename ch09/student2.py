
file = open('students.txt','r')

tt = []
wt = []

for line in file:
    data = line.split(',')
    print('{:8.2}\t{:9.2}\t{:5.2}\t{:5.2}'.format(data[0], data[1],data[2],data[3]))
    tt.append(int(data[2].strip()))
    wt.append(int(data[3].strip()))

print("키 평균{:10.2f}, 몸무게 평균{:8.2f}".format(sum(tt) / len(tt), sum(wt) / len(wt)))
file.close()