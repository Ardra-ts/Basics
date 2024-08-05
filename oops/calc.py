from abc import ABC 
class Calculator(ABC):
    def add(self):
        print("addition")
class Calculator1(Calculator):
    def sub(self):
        print("sub")

class Calculator2(Calculator):
    def multi(self):
        print("multi")

c=Calculator2()
c.add()
d=Calculator1()
d.sub()
d.add()
