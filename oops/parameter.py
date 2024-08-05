class school:
    def __init__(self,name,address):
        self.name1=name
        self.addr1=address

    def open(self):
        print("School name",self.name1)

    def close(self):
        prijnt("Address is ",self.addr1)

obj=school("name","addr")
print(obj.open())