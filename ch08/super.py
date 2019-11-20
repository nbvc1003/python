class Base:
    def __init__(self, name):
        print('Base.__init__')
        self.message = "안녕"
        print(name)
class Derived(Base):
    def __init__(self):
        print("Derived.__init__")
        # 명시적으로 부모 생성자를 콜해줘야 실행됨

        super().__init__('미호')
        print('메세지: {}'.format(self.message))



d1 = Derived()