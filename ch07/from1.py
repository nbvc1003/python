
# ch07.cal 내용을 전부 가져 와서 같은 파일내 함수 처럼 사용. * 사용을 지양
# 변수까지 가져 온다.
from ch07.cal import *  

# 특정 함수만 가져 온다. (권장사항)
from ch07.cal import plus, minus

print(plus(12,3))
print(minus(12,3))