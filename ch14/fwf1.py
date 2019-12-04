import pandas as pd

# 별도 구분자가 없는 덱스트 파일을 읽어 올때 사용
# widths=(10,2,5) 읽어오는 글자수 단위
fr = pd.read_fwf('data_fwf.txt', widths=(10,2,5),
                 names=('date','name','price'),
                 encoding='utf-8')
print(fr)


