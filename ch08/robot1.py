class Robot:
    def make(self):
        print("=======================================")
        print("난 로봇이야")

class DanceRobot(Robot):
    def dance(self):
        print("춤을춘다.")

class SingRobot(Robot):
    def sing(self):
        print("노래부른다.")
class DrawRobot(Robot):
    def draw(self):
        print("그림을 그린다.")

robots = [DanceRobot(), SingRobot(), DrawRobot()]

for bot in robots:
    bot.make()
    if isinstance(bot, DanceRobot):
        bot.dance()
    elif isinstance(bot, SingRobot):
        bot.sing()
    elif isinstance(bot, DrawRobot):
        bot.draw()



