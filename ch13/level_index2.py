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

print(stocks)
# 컬럼level에 이름 설정
stocks.columns.names = ['월','일']

# 컬럼기준의 합계
print(stocks.sum(level='월', axis=1))
print(stocks.sum(level='일', axis=1))

print(stocks.mean(level='월', axis=1))
print(stocks.mean(level='일', axis=1))