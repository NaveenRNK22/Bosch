class BankAccount:

    def __init__(self,Acc_no,Acc_name,ini_bal):
        self.Acc_no = Acc_no
        self.Acc_name = Acc_name
        self.balance = ini_bal
    
    def Deposit(self,amt):
        try:
            assert amt > 0
            self.balance += amt
        except AssertionError :
                print("Amount is negative")

    def Withdraw(self,amt):
        try:
            assert amt > 0
            if amt-self.balance <= 0:
                self.balance -= amt
            else:
                print("Insuffient Balance")

        except AssertionError :
                print("Amount is negative")

    def Transfer(self,amt,Acc_det):
        self.Withdraw(amt)
        Acc_det.Deposit(amt)
    
    def get_Balance(self):
        print("Balance:",self.balance)

    def __str__(self):
        return f"{self.Acc_name} hold the bank account number ({self.Acc_no})"

class SavingsAccount(BankAccount):
    def __init__(self,Acc_no,Acc_name,ini_bal):
        super().__init__(Acc_no,Acc_name,ini_bal)

    def apply_int(self,int_rate):
        self.balance += self.balance*int_rate
    
class CurrentAccount(BankAccount):
    def __init__(self,Acc_no,Acc_name,balance):
        super().__init__(Acc_no,Acc_name,balance)
    
    def Withdraw(self, amt):
        try:
            assert amt > 0
            self.balance -= amt
            print("Amount Withdrawn:",amt)
            print("New Balance:",self.balance)

        except AssertionError :
            print("Amount is negative")

class FixedDepositAccount(BankAccount):
    def __init__(self,Acc_no,Acc_name,balance):
        super().__init__(Acc_no,Acc_name,balance)
        
    
    def Create_FD(self,lockin_period):
        print(f"A fixed Deposit account is created for {lockin_period} months with amount {self.balance}")

class Bank:
    def __init__(self):
        self.accounts={}
    def create_acc(self,Acc_no,Acc_name,Type,ini_bal=0):
        if Acc_no not in self.accounts:
            if Type == "Savings":
                self.accounts[Acc_no]= SavingsAccount(Acc_no,Acc_name,ini_bal)
            elif Type == "Current":
                self.accounts[Acc_no]= CurrentAccount(Acc_no,Acc_name,ini_bal)
            elif Type == "Fixed":
                self.accounts[Acc_no]= FixedDepositAccount(Acc_no,Acc_name,ini_bal)
            else:
                return False
        return True
    def get_acc(self,Acc_no):
        return self.accounts.get(Acc_no,None)
    

bank = Bank()
bank.create_acc("001","Vinesh","Savings",10000)
bank.create_acc("002","Sujan","Current",5000)

#deposits, withdraw and get balance
print("Savings Account Deposit")
acc1 = bank.get_acc("001")
acc1.Withdraw(2000)
acc1.get_Balance()

print("Current Account Withdrawl")
acc2=bank.get_acc("002")
acc2.Deposit(1000)
acc2.get_Balance()

#Interest in Savings
print("Savings Account Interest addition")
acc1.apply_int(0.04)
acc1.get_Balance()

#Overdraft Facility in Current account
print("Currennt Account Overdraft facility addition")
acc2.Withdraw(20000)
acc2.get_Balance()

#Fixed Deposit
bank.create_acc("003","Rogith","Fixed",15000)
acc3 = bank.get_acc("003")
acc3.Create_FD(2)

#Transfer b/w accounts
a1 = input("Enter your Account  no:")
a2 = input("Enter Recievers Account no:")
amt = int(input("Enter Amount to send:") )


send=bank.get_acc(a1)
rec=bank.get_acc(a2)

print("Balance before Transfer")
send.get_Balance()
rec.get_Balance()

send.Transfer(amt,rec)

print("Balance after Transfer")
send.get_Balance()
rec.get_Balance()



