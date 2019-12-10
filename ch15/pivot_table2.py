import pandas as pd

df = pd.read_csv('tips.csv')
print(pd.pivot_table(df, values=['tip','total_bill'], index=['sex','day'],
                     columns='smoker', aggfunc=['sum',len]))

print('=========================================================================')
print(pd.pivot_table(df, values=['tip'], index=['sex','day'],
                     columns='smoker', aggfunc=['sum','mean',len]))

