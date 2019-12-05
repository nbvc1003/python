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

# writer = pd.ExcelWriter('s1.xlsx')
# data.to_excel(writer, sheet_name='fruit')
# writer.save()

writer = pd.ExcelWriter('s2.xlsx')
data.to_excel(writer, sheet_name='fruit', header=False)
writer.save()