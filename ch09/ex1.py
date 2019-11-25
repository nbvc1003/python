

f1 = open("test.txt", 'w')
f1.write("Life is too short")
f1.close()
# /// 위와 동일하다.
# with open("test.txt", 'w') as f1:
#     f1.write("Life is too short")
# ///


f2 = open("test.txt", 'r')
print(f2.read())
f2.close()
