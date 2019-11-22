# chichen.txt 매출 총계와 평균 매출 출력

file = open('chicken.txt', 'r',encoding='utf-8')

nums = []
for line in file:
    # nums.append(int( line.split(": ")[1].strip()))
    nums.append(int(line.split(":")[1]))
print(nums)
sum = sum(nums)
print("매출 총계 {} 평균 매출  {}".format(sum, sum/len(nums)))

