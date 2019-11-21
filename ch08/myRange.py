
# 이터레이터 타입을 직접 구현 했을경우
class Myrange:
    def __init__(self, start, end):
        self.current = start
        self.end = end
    def __iter__(self):
        return self
    def __next__(self):
        if self.current < self.end:
            current = self.current
            self.current += 1
            return current
        else:
            raise StopIteration()

for i in Myrange(0,5):
    print(i)
    