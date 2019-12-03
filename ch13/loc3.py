import pandas as pd

data = {
        "2015": [9904312, 3448737, 2890451, 2466052], # 열은 같은 데이터 타입
        "2010": [9631482, 3393191, 2632035, 2431774],
        "2005": [9762546, 3512547, 2517680, 2456016],
        "2000": [9853972, 3655437, 2466338, 2473990],
        "지역": ["수도권", "경상권", "수도권", "경상권"],
        "2010-2015 증가율": [0.0283, 0.0163, 0.0982, 0.0141]
        }

column = ["지역","2015","2010","2005","2000","2010-2015 증가율"]
index = ["서울","부산","인천","대구"]

df = pd.DataFrame(data, index=index, columns=column)
print(df)
print("--------------------------------------------------")
# 0행
print(df.iloc[0])

#1행 1열
print(df.iloc[1,1])

# 0,1행, 마지막 열
print(df.iloc[[1,2], -1])
print(df.iloc[:2, -1])# 둘다 같다


# 0행 데이터를 2배로 수정
df.iloc[0] = df.iloc[0] *2
print(df)
