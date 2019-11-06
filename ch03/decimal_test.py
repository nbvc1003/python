from decimal import *

sum = Decimal('0.0')
delta = Decimal('0.1') # 문자열을 넣어야 한다.

for i in range(0,1000):
 sum += delta
print("sum:" , sum)
