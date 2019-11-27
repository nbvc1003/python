import re

p = re.compile(r'(?P<name>\w+)\s+(?P<tel>\d+[-]\d+[-]\d+)')
m = p.sub('\g<tel> \g<name>', 'park 010-1234-5678')
print(m)
m = p.sub('\g<2> \g<1>', 'park 010-1234-5678')
print(m)