class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance): 
        self.int_rate=int_rate
        self.balance=balance
    def deposit(self, amount):
        self.balance+=amount
        return self
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance-=5
        return self
    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self
    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self
account1=BankAccount(.05,1000)
account2=BankAccount(.02,7000)
account1.deposit(100).deposit(200).deposit(400).withdraw(60).yield_interest().display_account_info()
account2.deposit(100).deposit(200).withdraw(60).withdraw(50).withdraw(40).withdraw(20).yeild_interest().display_account_info()