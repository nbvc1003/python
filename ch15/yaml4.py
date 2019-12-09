import yaml

fruits = [{"이름":"사과", "가격":2000,"색":"빨강"},
          {"이름":"참외","가격":3000,"색":"노랑"},
          {"이름":"키위","가격":1200,"색":"연두"}]

# yaml 변경하여 출력
# yaml 형식으로 읽어서  이름 가격 색출력

temp = yaml.dump(fruits, allow_unicode=True)
print(temp)
datas = yaml.safe_load(temp)

for i in datas:
    print("이름 :"+i['이름'],"가격 :" + str(i['가격']))



