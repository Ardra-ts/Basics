class d1:
    x='hi'
    def display(self):
        print(self.x)

class d2(d1):
    y=4
    z=8
    def sum(self):
        print(self.y+self.z)

class d3(d2):
    def dis(self):
        print("Grand")

obj = d3()
obj.display()
obj.sum()