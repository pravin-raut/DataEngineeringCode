class Account:
    Bank="Welcome to Pravin Bank"

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f"Owner is: {self.owner} \nBalance is: {self.balance}"

    def deposit(self,invest):
        self.balance=self.balance+invest
        print("Successfully deposited {} and total balance is   `11{}".format(invest,self.balance))
        return self.balance

    def withdrawl(self,remove):
        if (self.balance>=remove):
            self.balance=self.balance-remove
            print("Successfully withdrawn {} and total balance is {}".format(remove,self.balance))
        else:
            print("Not enough money to withdraw total balance is {}".format(self.balance))
        return self.balance

acc=Account('Pravin',1000)

print(acc)
print(acc.owner)
print(acc.balance)
acc.deposit(100)
acc.withdrawl(100)
acc.deposit(1000)

acc.withdrawl(10000)
