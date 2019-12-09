import yaml
members = [{'이름':'세정','나이':22},
           {'이름':'강다니엘','나이':23},
           {'이름':'쯔위','나이':25}]

# 데이터를 yaml 형식으로 변환
yaml_str = yaml.dump(members, allow_unicode=True)
print(yaml_str)
# 문자열을 yaml 형식으로 해석
data = yaml.safe_load(yaml_str)
for m in data:
    print('이름:{}.나이:{}'.format(m['이름'],m['나이']))
