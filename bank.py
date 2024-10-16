class Account:
    def __init__(self,balance,acc_no):
        self.balance=balance
        self.acc_no=acc_no

    def debit(self,amount1):
        self.balance-=amount1
        self.get_balance()

    def credit(self,amount2):
        self.balance+=amount2
        self.get_balance()

    def get_balance(self):
        print("the balance is",self.balance)


acc1=Account(10000,234415)
acc1.debit(1000)
acc1.credit(2000)