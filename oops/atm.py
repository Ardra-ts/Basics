class atm:
    def __init__(self,name,acc_no):
        self.name=name
        self.acc_no=acc_no
        self.balance=0
    def display(self):
        print()
        print("------Account details------")
        print("Account holder name : ",self.name)
        print("Account Number : ",self.acc_no)

    def deposit(self,dep):
        self.dep=dep
        self.balance=self.dep+self.balance
        print("Amount added ")
    
    def withdraw(self,w):
        if w<self.balance:
            self.balance=self.balance-w
            print("Amount withdraw ")
        else :
            print("Insufficient balance")

    def bal1(self):
        return self.balance


name = input("Enter the name : ")
acc_no = int(input("Enter the account number : "))
obj=atm(name,acc_no)
obj.display()

print('''1.Deposit
2.Withdraw
3.Display
4.Exit ''')

while(True):
    n=int(input("Enter the choice "))
    if n==1:
        dep=int(input("Enter the amount : "))
        obj.deposit(dep)
    elif n==2:
        w=int(input("Enter the amount : "))
        obj.withdraw(w)
    elif n==3:
        print(obj.bal1())
    elif n==4:
        print("Exit")
        break
    else:
        print("Invalid input")

