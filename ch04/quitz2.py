
def multiply_by_two():
 global x
 x = x * 2

def multiply_by_three():
 y = 2
 y = y * 3

x = 2
multiply_by_two()
print(x)
y = 2
multiply_by_three()
print(y)
