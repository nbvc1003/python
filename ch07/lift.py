class Lift:
    def __init__(self, current_floor = 0):
        self.current_floor = current_floor

    def setFloor(self,floor):
        self.current_floor = floor

    def getFloor(self):
        return self.current_floor

    def print(self):
        print("현재 {}층 입니다. ".format(self.current_floor))

lift = Lift()
lift.print()
# 3층으로 set
lift.setFloor(3)
lift.print()
