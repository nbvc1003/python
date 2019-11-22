num = "1.2.3.4.5.6"

sp1 = num.split(".")
print(sp1)

num = '1 2 3 4 5 6'
sp1 = num.split(" ")
print(sp1)

num = '1 \t2 \t\t3 \n4 \t\t5 6'
sp1 = num.split() # 인자 생략시 문자이외 \t, \n , 공백등 포함해서 분리 문자로 인식한다.
print(sp1)
