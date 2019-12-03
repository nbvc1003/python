import pandas as pd
s1 = pd.Series([9904312, 3448737, 2890451, 2466052],
                index=["서울", "부산", "인천", "대구"])
s2 = pd.Series({"서울": 9631482, "부산": 3393191,
                "인천": 2632035, "대전":1490158})

rs = (s1 - s2)/s2 * 100
# 조건을 넣어서 출력
print(rs[rs.notnull()]) 

rs["부산"] = 1.63 # 데이터 수정 (기존 인덱스에 값을 넣는다. )
rs["대구"] = 1.41 # 데이터 추가 (없는 인덱스에 값을 넣는다. )

print(rs[rs.notnull()])
del rs["서울"] # 데이터 삭제
print(rs[rs.notnull()])