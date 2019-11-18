from ch07.car1 import Car

mycar = Car()
print(mycar.color)
mycar.backward()

yourcar = Car()
yourcar.color = "blue"

print(mycar.color)
print(yourcar.color)
yourcar.forward()


print(mycar.test)
mycar.test = 2.0
print(mycar.test)
print(yourcar.test)