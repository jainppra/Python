class Account:
    
    def __init__(self,owner,balance=0):
        self.owner=owner
        self.balance=balance
        
    def __str__(self):
        return "Owner : {} \nBalance : {}".format(self.owner,self.balance)
        
    def deposit(self,amount):
        if amount>0:
            self.balance +=amount
            print("deposit Successfully")
        else:
            print("Enter valid amount")
            
            
    def withdraw(self,amount):
        if amount>self.balance:
            print("Fund not available")
        else:
            balance -= amount
            print("Successfully withdraw")
            
    def check_balance(self):
        print(self.balance)
            
ac1 = Account("Prateek",1000)

print(ac1)




