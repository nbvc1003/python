
class User:
    def __init__(self, name, emaill, password):
        self.name = name
        self.email = emaill
        self.password = password
    #자기소개
    def introduce(self):
        print("이름은 {}, 이메일은 {} ".
              format(self.name, self.email))

    def introduce_twice(self):
        self.introduce(); self.introduce();


u1 = User('하니', 'adfs@xcvxzvc.com', '1234')
u1.introduce()
u1.introduce_twice()
