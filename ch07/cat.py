# Cat __init__(name)
# speck 야옹
# drink (self, food) # ㅌㅌ가 ㅌㅌㅌ를 마신다.


class Cat:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print("야옹")
    def drink(self, food):
        print("{}가 {}를 마신다. ".format(self.name, food))


cat1 = Cat("나비")
cat2 = Cat("홍이")
cat1.speak();cat1.drink("물");cat2.speak();cat2.drink('주스')

Cat.speak(cat2); Cat.drink(cat1, "막걸리")