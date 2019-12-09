from pandas import Series
import pandas as pd


s1 = Series([84900, 818000, 1756], index=['다음',"네이버", "넥슨"])
s2 = Series([86100, 871000, 1776,295000], index=['다음',"네이버", "넥슨", "NC"])

# 두 데이터를 붙인다.
print(pd.concat([s1,s2])) # 상하 , 수직
print(pd.concat([s1,s2],axis=1, sort=True)) # 좌우로 , 소팅해서 붙인다. ( 영문, 한글 순)
print(pd.concat([s1,s2],axis=1, sort=False)) # 좌우로 , 소팅없이

# inner 양쪽에 모두 존재하는 데이터만 합친다. (교집합) default 는 outer (합집합)
print(pd.concat([s1,s2], axis=1, sort=True, join='inner'))
print(pd.concat([s1,s2], axis=1, keys=['2017-03-19','2017-03-20'], sort=True))
# print(pd.concat([s1,s2], axis=1, keys=['2017-03-19','2017-03-20'], join_axes=[['다음','네이버','넥슨','NC']]))
print(pd.concat([s1,s2],axis=1,sort=True).loc[['다음','네이버']]) # 좌우로 정렬해서 다음, 네이버 행만



