# stock.csv 읽어서 stock.xlsx로 저장
# 날짜 11월 12월 로 만들고 
# 저장 할때는 header= true / index는 삭제

import pandas as pd

# names : 컬럼명
csvDf = pd.read_csv('stock.csv', header=None, names=['날짜','11월','12월'])


# csvDf = csvDf.T
print(csvDf)

write = pd.ExcelWriter('stock2.xlsx')
csvDf.to_excel(write, sheet_name='Sheet1', index=False)
write.save()