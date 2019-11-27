import re
p = re.compile("Crow|Serve") # Crow 또는 Serve 
m = p.match('CrowHello')
print(m)

# ^ -> 문자열 시작했는지
p = re.search('^Life','Life is too short')
print(p)

p = re.search('^Life','My Life is too short')
print(p)

