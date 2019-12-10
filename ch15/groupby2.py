
import pandas as pd


# smoker 기준 total bill출력
df = pd.read_csv('tips.csv')
print(df)
print('===================================================================')
gp = df['total_bill'].groupby(df['smoker'])

for totalBill, smoke in gp:
    print(totalBill)
    print(smoke)


print('===================================================================')