
from abc import *
class Employ(metaclass=ABCMeta):
    def __init__(self, name):
        self.name = name
    @abstractmethod
    def cal_sal(self):
        pass
    def bonus(self):
        self.sal = self.cal_sal()
        self.bonus = self.sal * 0.1
    def prn(self):
        print("------------------------------")
        print("이름 : {}".format(self.name))
        print("급여 : {0:.2f}".format(self.sal))
        print("보너스 {0:.2f}".format(self.bonus))

class SalaryMan(Employ):
    def __init__(self, name, annual):
        super().__init__(name)
        self.annual = annual
    def cal_sal(self):
        return self.annual/12
    def prn(self):
        super().prn()
        print("연봉 : {}".format(self.annual))
class HourlyMan(Employ):
    def __init__(self, name, work_hour, money_per_hour):
        super().__init__(name)
        self.work_hour = work_hour
        self.money_per_hour = money_per_hour
    def cal_sal(self):
        return self.work_hour * self.money_per_hour
    def prn(self):
        super().prn()
        print("단가 :{}".format(self.money_per_hour))
        print("근무 : {}시간".format(self.work_hour))


s1 = SalaryMan("유느님", 5000000)
h1 = HourlyMan("신동엽", 15,3000000)

emps = [s1, h1]

for e in emps:
    e.bonus()
    e.prn()





