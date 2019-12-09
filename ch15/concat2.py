import pandas as pd

s1 = pd.Series([9904312, 3448737, 2890451, 2466052],
                index=["서울", "부산", "인천", "대구"])
s2 = pd.Series({"서울": 9631482, "부산": 3393191,
                "인천": 2632035, "대전":1490158})

print(s1)
print(s2)
print("================================")
# 상하로 합치기
print(pd.concat([s1,s2]))
# 좌우로 합치기 sort True
print(pd.concat([s1,s2],axis=1,sort=True))
# 좌우로 inner
print(pd.concat([s1,s2],axis=1,sort=True,join='inner'))
# 좌우로 컬럼명 2018, 2019
print(pd.concat([s1,s2],keys=['2018','2019'], axis=1,sort=True))

print(pd.concat([s1,s2],keys=['2018','2019'], join_axes=[["서울","부산","인천","대구","대전"]],  axis=1))

print(pd.concat([s1,s2],axis=1,sort=True,keys=['2018','2019']).loc[['서울','부산']])

