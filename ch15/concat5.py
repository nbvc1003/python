import pandas as pd

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
        "2015": [9904312, 3448737, 2890451, 2466052], # 열은 같은 데이터 타입
        "2010": [9631482, 3393191, 2632035, 2431774],
        "2005": [9762546, 3512547, 2517680, 2456016],
        "2000": [9853972, 3655437, 2466338, 2473990],
        }

column2 = ["2015","2010","2005","2000"]
index2 = ["서울","부산","인천","대전"]

# DataFrame 생성방법
df2 = pd.DataFrame(data2, index=index2, columns=column2)



# df1, df2 inner join Nan
print(pd.concat([df1,df2], axis=1,sort=True).fillna('-'))
print(pd.concat([df1,df2], axis=1, sort=True, join='inner').fillna('-'))

# df1 index 기준 Nan
print(pd.concat([df1,df2, df1.reindex(df1.index)], axis=1, sort=True, join='inner'))
