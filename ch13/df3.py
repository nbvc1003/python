import pandas as pd



items = {'code': [1,2,3,4,5,6],
        'name': ['apple','watermelon','oriental melon', 'banana', 'lemon', 'mango'],
        'manufacture': ['korea', 'korea', 'korea','philippines','korea', 'taiwan'],
        'price':[1500, 15000,1000,500,1500,700]
         }

column = ['code','name','manufacture','price']

data = pd.DataFrame(items, index=items['code'], columns=column)

print(data)