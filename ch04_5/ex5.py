


# 재품명 매출 합계 평균(소수점2) 매출

def maechul (name, *val):
    sum = 0
    for i in val:
        sum += i
    print('{}의 매출 합계 {}, 평균{:0.2f}'.format(name,sum, sum/len(val)))

maechul("TV",100, 120, 210)
maechul("냉장고",200, 340, 760)
maechul("세탁기",500, 670, 340)