import time
from dateutil.parser import parse



# dateutil.parser 문자를 datetime 형식으로 읽어온다. (형식을 자동으로 인식하여 가져 온다.)
# strptime 와 유사한 기능
dt = parse('2019-12-16')
print(dt, type(dt))

