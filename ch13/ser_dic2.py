import pandas as pd

fruit = pd.Series([4000, 3000, 3500, 2000], index=['apple','mellon','orange','kiwi'])

# apple가 포함되었는지 , 안되었는지 확인
print('apple' in fruit, 'apple' not in fruit)
# banana가
print('banana' in fruit, 'banana' not in fruit)
print('-----------------------------------------')
# index : value 형식으로 출력
for k,v in fruit.items():
    print(k,' :',v)
print('-----------------------------------------')
#데이터를 딕셔너리 형 식으로 만들어서fruit2 를 만들고 fruit2출력
fruit2 = pd.Series({'apple':4000,'mellon':3000,'orange':3500,'kiwi':2000})
print(fruit2)
