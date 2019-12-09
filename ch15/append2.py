import pandas as pd
import numpy as np
# dictionary
data1 = {
        "2015": [9904312, 3448737, 2890451, 2466052], # 열은 같은 데이터 타입
        "2010": [9631482, 3393191, 2632035, 2431774],
        "2005": [9762546, 3512547, 2517680, 2456016],
        "2000": [9853972, 3655437, 2466338, 2473990],
        }

column1 = ["2015","2010","2005","2000"]
index1 = ["서울","부산","인천","대구"]
# DataFrame 생성방법
df1 = pd.DataFrame(data1, index=index1, columns=column1)

data2 = {
        "2015": [8904312, 2448737, 1890451, 1466052], # 열은 같은 데이터 타입
        "2010": [8631482, 2393191, 1632035, 1431774],
        "2005": [8762546, 2512547, 1517680, 1456016],
        "2000": [8853972, 2655437, 1466338, 1473990],
        }

column2 = ["2015","2010","2005","2000"]
index2 = ["서울","부산","인천","대전"]
df2 = pd.DataFrame(data2, index=index2, columns=column2)

# df1 + df2
# append
# combine first
# combine minimum

print(df1 + df2)
print(df1.append(df2))
print(df1.combine_first(df2))


# 사전에 NaN처리 하고 나서 작업 필요..
take_smaller = lambda s1, s2: s1 if s1.sum() < s2.sum() else s2
take_bigger = lambda s1, s2: s1 if s1.sum() > s2.sum() else s2

print(df1.combine(df2, take_smaller))
print(df1.combine(df2, take_bigger))





