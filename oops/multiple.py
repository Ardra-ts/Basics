class d1:
    x='hi'
    def display(self):
        print(self.x)

class d2:
    y=4
    z=8
    def sum(self):
        print(self.y+self.z)


class Childclass(d1,d2):
    def data(self):
        print("Display")


obj=Childclass()
obj.display()
obj.sum()
obj.data()