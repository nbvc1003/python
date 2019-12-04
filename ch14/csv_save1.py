import pandas as pd

items = {'apple':{'count':10,'price':1500},
        'banana':{'count':5,'price':15000},
        'mellon':{'count':7,'price':1000},
        'kiwi':{'count':20,'price':500},
        'mango':{'count':30,'price':1500},
        'orange':{'count':4,'price':700}
         }

data = pd.DataFrame(items).T
print(data)



data.index.name = 'fruit' # 인덱스 컬럼에 이름을 부여함
data = data.reset_index() # 새로운 인덱스 추가
print(data)
# data.to_csv('data.csv',header=False, index=False)
data.to_csv('data.csv',index=False)

