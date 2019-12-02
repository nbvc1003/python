import pandas as pd

s1 = pd.Series([9904312, 3448737, 2890451, 2466052],
                index=["서울", "부산", "인천", "대구"])
s2 = pd.Series({"서울": 9631482, "부산": 3393191, "인천": 2632035, "대전":1490158})

# index를 참고하여 같은것이 없으면 NaN
ds = s1 - s2
print(ds)

# 단순 값의 배열간의 연산 index상관없이 순서대로 연산
print(s1.values - s2.values)

print(ds.notnull()) # 값이 있으면 True
print(ds[ds.notnull()]) # True인 값만 출력

rs = (s1 - s2) / s2 * 100
print(rs)
print(rs[rs.notnull()])

