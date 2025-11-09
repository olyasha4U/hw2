1
class BankAccount:
    def __init__(self, account_number=0, balance=0):
        self.account_number=account_number
        self.balance=balance

    def deposit(self, money):
        self.balance += money
        print(f"На рахунок зараховано {money} грн. Поточний баланс: {self.balance} грн.")

    def withdraw(self, money):
        if self.balance >= money:
            self.balance -= money
            print(f"З рахунку знято {money} грн. Залишок: {self.balance} грн.")
        else:
            print(f"Недостатньо коштів! Ваш баланс: {self.balance} грн.")
a1=1000
a2=200
a3=801
account=BankAccount()

account.deposit(a1)
account.withdraw(a2)
account.withdraw(a3)
print(account)
