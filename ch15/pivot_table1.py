import pandas as pd

df = pd.read_csv('tips.csv')


# 데이터, 인덱스, 컬럼
print(pd.pivot_table(df, values=['tip','total_bill'], index=['sex','day'],
                     columns='smoker'))

# pivot_table 의 기본적으로 값을 묶을때 평균 함수를 사용한다.
# index sex, smoker, column day  value : tip
print(pd.pivot_table(df, values='tip',index=['sex','smoker'],columns='day', margins=True))
# margins=True -> 디폴트 전체 평균 추가
print('==========================================================================================')

# aggfunc = 'sum' 샛팅시 합계값 -> margin =True 로 나오는 all 값 또한 전체 합계값
print(pd.pivot_table(df, values='tip',index=['sex','smoker'],columns='day', margins=True, aggfunc='sum'))