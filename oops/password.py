class user:
    password=[]
    def __init__(self,,pswd):
        self.password.append(pswd)
    def get_pswd(self):
        return self.password[=1]
    def is_crct(self,pswd):
        if pswd=self.get_pswd():
            return True
        else:
            return False
    def reset(self,pwd):
        if pwd not in self.password:
            self.password.append(pwd)
            print("Password reset successfully!!!")
        else:
            print("Cannot reset password!!!")
        
pwd = input("Enter the password")
