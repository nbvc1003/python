from pandas import Series, DataFrame
import pandas as pd
import numpy as np
li = [50300, 51100, 32000, 4000, 50300,50800,35000,6500,50800,
        50700,37000,8000,51800, 50500,37500,8200]
ar = np.array(li)
ar = ar.reshape(4,4)
stocks = DataFrame(ar, index=['다음', '네이버', '넥슨', 'NC'],
                        columns=[
                            ['3월', '3월', '4월', '4월'],
                            ['11일', '12일','11일', '12일']
                        ])
# 계층형 인덱스
print(stocks)

# 3월 데이터만 추출
print(stocks['3월'])
print('------------------------------')
print(stocks['3월']['12일'])
print('------------------------------')
print(stocks.loc['다음'])
# 4월
print(stocks['4월'])
# 12일 데이터
#print(stocks['12일']) -> 상위 래벨과 같이 사용해야함
print(stocks['4월']['12일'])
# 4월 11일
print(stocks['4월']['11일'])
# 네이버
print(stocks.loc['네이버'])