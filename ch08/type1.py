#정적 클래스 : 클래스를 만들고 계속 사용 

class StaticClass1:
    attr = "정적 클래스"

s1 = StaticClass1(); s11 = StaticClass1()
print(s1.attr)

# 동적 클래스 : 한번 만들어 사용하고 끝
s2 = type('DynamicCl', (), {'attr':'동적 클래스'})
print(s2.attr)
# 위에서 사용되고 사라진다. 
# s21 = DynamicCl() # 안된다.
