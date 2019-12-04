import pandas as pd

excel1 = pd.ExcelFile("excel.xlsx")
print(type(excel1))
# pandas.io.excel._base.ExcelFile 형식으로 받는 방법
df_excel1 = excel1.parse("Sheet1", index_col=0)
print(df_excel1)

# DataFrame 으로 바로 받는 받법
df = pd.io.excel.read_excel('excel.xlsx', sheet_name="Sheet1",
                            index_col=0)
print(df, type(df))
# 위와 동일
df2 = pd.read_excel('excel.xlsx', sheet_name="Sheet1",
                            index_col=0)
print(df2, type(df2))