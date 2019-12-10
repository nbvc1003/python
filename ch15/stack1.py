import pandas as pd
import numpy as np

stock1 = {
        '2017-03-20': [84900, 1756,292000],
        '2017-03-21': [86100, np.nan,295000]}
df1 = pd.DataFrame(stock1,index=['다음',"넥슨", "NC"])
print(df1)
print("==================")
# .stack() : 컬럼을 2번째 인덱스로 변경 되고 원래 인덱스는 그대로
print(df1.stack())
print("==================")
# .stack() : 컬럼을 1번째 인덱스로 변경 되고 원래 인덱스는 2번째 인덱스로 
print(df1.unstack())
