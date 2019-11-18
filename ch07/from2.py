
from ch07.ex1 import *
print(mypi)


# from 을 사용하여 면적을구한다
from ch07.ex1 import area
print(area(10))
print(area(8))

# 임포트 함수 명을 변경할수 있다.
from ch07.ex1 import area as ar
from ch07.cal import plus as p
print(ar(4))
print(p(4,5))

