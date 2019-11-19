class User:
    def initialize(self, name, email, password):
        #self가 붙어 있는 변수는 맴버 변수 이다. == this
        self.name = name
        self.email = email
        self.password = password


    def print1(self):
        print(self.name, self.email, self.password)


user1 = User()
user1.initialize("Young", "young@codeit.kr", "123456")
user2 = User()
user2.initialize("Yoonsoo", "yoonsoo@codeit.kr","abcdef")
# user3 = User()
# user3.name = "Taeho"
# user3.email = "taeho@codeit.kr"
# user3.password = "123abc"
# user4 = User()
# user4.name = "Lisa"
# user4.email = "lisa@codeit.kr"
# user4.password = "abc123"
user1.print1();user2.print1()
# User.initialize(user1, "yong111","1234","11111")
# User.print1(user1)

