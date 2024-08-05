class emp:
    def data(self,name,id_no,sal):
        self.name=name
        self.id_no=id_no
        self.sal=sal

    def bal(self):
        if self.sal<10000:
            self.da=self.sal*0.2
            self.hra=self.sal*0.25
            self.pf=self.sal*0.05
        else:
            self.da=self.sal*0.1
            self.hra=self.sal*0.15
            self.pf=self.sal*0.03
        self.net=self.da+self.hra-self.pf

    def display(self):
        print()
        print("Name : ",self.name)
        print("Emp code :",self.id_no)
        print("Basic salary :",self.sal)
        print("DA :",self.da)
        print("HRA :",self.hra)
        print("PF :",self.pf)
        print("Net salary :",self.net)
    

name = input("Enter the name ")
id_no = int(input("Enter the id "))
sal = int(input("Enter the basic sal "))
obj=emp()
obj.data(name,id_no,sal)
obj.bal()
obj.display()