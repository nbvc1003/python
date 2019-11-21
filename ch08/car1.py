# Car color, disp, prn()
# Sonata + passerger 소, 말
# Bentz + unit 블랙박스, 네비
# SM5 + factory , 군산, 부산
class Car:
    def __init__(self, color, disp):
        self.color = color;
        self.disp = disp

    def prn(self):
        print("=================================================")
        print("색깔 :{}, 베기량:{}".format(self.color, self.disp))


class Sonata(Car):
    def __init__(self, color, disp, passenger):
        super().__init__(color, disp)
        self.passenger = passenger

    def prn(self):
        super().prn()
        print("승객 : {}".format(self.passenger))


class Bentz(Car):
    def __init__(self, color, disp, unit):
        super().__init__(color, disp)
        self.unit = unit

    def prn(self):
        super().prn()
        print("장비 : {}".format(self.unit))


class SM5(Car):
    def __init__(self, color, disp, factory):
        super().__init__(color, disp)
        self.factory = factory

    def prn(self):
        super(SM5,self).prn()
        print("공장 : {}".format(self.factory))


st1 = Sonata('노랑', 4, '소')
bz1 = Bentz('검정', 6, '네비')
sm1 = SM5('흰', 4, '군산')

st1.prn()
bz1.prn()
sm1.prn()
