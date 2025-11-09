# 1
# class BankAccount:
#     def __init__(self, account_number=0, balance=0):
#         self.account_number=account_number
#         self.balance=balance
#
#     def deposit(self, money):
#         self.balance += money
#         print(f"На рахунок зараховано {money} грн. Поточний баланс: {self.balance} грн.")
#
#     def withdraw(self, money):
#         if self.balance >= money:
#             self.balance -= money
#             print(f"З рахунку знято {money} грн. Залишок: {self.balance} грн.")
#         else:
#             print(f"Недостатньо коштів! Ваш баланс: {self.balance} грн.")
# a1=1000
# a2=200
# a3=801
# account=BankAccount()
#
# account.deposit(a1)
# account.withdraw(a2)
# account.withdraw(a3)
# print(account)
# 2
# class Car:
#     def __init__(self, make="Benz", model="Patent-Motorwagen", year=1885 ):
#         self.make=make
#         self.model=model
#         self.year=year
#         self.info=[]
#     def get_info(self):
#         print(f"Марка: {self.make}, Модель: {self.model}, Рік: {self.year}")
#
#
# car=Car()
# car.get_info()
# 3
# class Employee:
#     def __init__(self, name="Alex", position="manager", salary=65000):
#         self.name=name
#         self.position=position
#         self.salary=salary
#     def get_salary_info(self):
#         print(f"Заробітна плата {self.name}: {self.salary}")
# employee=Employee()
# employee.get_salary_info()
4
class Rectangle:
    def __init__(self, width=4, height=6):
        self.width=width
        self.height=height
    def calculate_area(self):
        area=self.height*self.width
        print(f"Rectangle area ={area}")
    def calculate_perimeter(self):
        perimeter=self.height+self.width
        print(f"Rectangle perimeter={perimeter}")
rec=Rectangle()
rec.calculate_area()
rec.calculate_perimeter()
