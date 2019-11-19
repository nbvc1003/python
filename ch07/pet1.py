#class Pet name 셋팅

# sleep ㅌㅌ가잠을 잡니다. 
# exat ㅌㅌr가 약간의 음식을 먹습니다. . xx가 더달래요

class Pet:
    def __init__(self, name):
        self.name = name
    def sleep(self):
        print("{}가 잠을 잡니다. ".format(self.name))
    def exat(self):
        print("{}가 약간의 음식을 먹습니다. {}가 더달래요".format(self.name, self.name))

if __name__ == "__main__":
    p1 = Pet("나비")
    p1.sleep()
    p1.exat()




