import pandas as pd


df1 = pd.read_excel('Koweps_Codebook.xlsx', sheet_name="직종 코드", index_col=0)
print(df1)