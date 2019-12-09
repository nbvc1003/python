import yaml


fruits = """

data :
    -
        이름 : 사과
        가격 : 1000
    -
        이름 : 자두
        가격 : 1200
    -
        이름 : 복숭아
        가격 : 1500

"""


datas = yaml.safe_load(fruits)

for i in datas['data']:
    print(i['이름'],i['가격'])

