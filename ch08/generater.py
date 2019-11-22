def YourRange(start, end):
    current = start
    while current < end:
        yield current
        current += 1
    

for i in YourRange(0, 5):
    print(i)
