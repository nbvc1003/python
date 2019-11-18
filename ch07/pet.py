
# Pet class 생성
# cat , dog,
# cat : name, age, 작성 출력
# dog : name 를 넣고 이름과 나이 출력


class Pet:
    def __init__(self):
        self.name = ""
        self.age = 0


cat = Pet()
cat.name = "고양이"
cat.age = 1
dog = Pet()
dog.name = "강아지"
print(cat.name, cat.age, dog.name, dog.age)
