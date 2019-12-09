import yaml

yaml_str = """
# 정의
color_def:
     - &color1 "#FF0000"
     - &color2 "#00FF00"
     - &color3 "#0000FF"
#     
color:
     title: *color1
     body: *color2
     link: *color3
"""
# & 실제 값 내용, * 링크  -> '&' 주소에 값을 선언 , '*' 해당주소의 데이터를 읽는다.
data = yaml.safe_load(yaml_str)
print("title = ", data['color']['title']) #
print("body = ", data['color']['body'])
print("lick = ", data['color']['link'])


