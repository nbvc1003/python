import pandas as pd
import numpy as np

fr1 = pd.DataFrame(np.arange(9).reshape(3,3), index=['a','c','d'],
                  columns=['Ohio','Texsas','Califonia'])
print(fr1)

fr2 = fr1.reindex(['a','b','c','d'])
# 옵션 진자에 값을 넣지 않을 경우 없는 인덱스는 NaN
print(fr2)

