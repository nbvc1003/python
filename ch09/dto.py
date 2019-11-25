class Person:
    def setNum(self, num):
        self.num = num
    def setName(self, name):
        self.name = name
    def getNum(self):
        return self.num

    def getName(self):
        return self.name

    def toString(self):
        return "{'번호:"+str(self.num)+", 이름:" + self.name+"}"