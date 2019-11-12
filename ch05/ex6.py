

numbers = [1,2,3,4,5]

result = []
for n in numbers:
    if n % 2 == 1:
        result.append(n*2)

print(result)

# 내포 함수
# 위 와 동일한 결과
result = [ k*2 for k in numbers if(k%2==1)]
print(result)

