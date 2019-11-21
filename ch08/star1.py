class Star:
    def attack(self):
        print("스타의 어택")
class Terran(Star):
    def attack(self):
        print("태란의 어택")

class Zerg(Star):
    def attack(self):
        print("저그의 어택")


star = [Star(), Terran(), Zerg()]

for s in star:
    s.attack()


