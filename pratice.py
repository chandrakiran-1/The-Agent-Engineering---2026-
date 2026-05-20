class Calculator:
    @staticmethod
    def multiply(a,b):
        return a*b
print(Calculator.multiply(2,3))


class Student:
    def __init__(self ,name):
        self.name = name
    def show(self):
        print("name : ", self.name)
std = Student("chandu")
std.show()

class Employee:
    company = "google"
    def __init__(self, name):
        self.name = name 
    @classmethod
    def Change_company(cls , new_company):
        cls.company = new_company
print(Employee.company)
Employee.Change_company("microsoft")
print(Employee.company)

class Math:
    @staticmethod
    def add(a,b):
        return a+b
print(Math.add(2,4))

class Math1:
    def __init__(self, a,b):
        self.a =a
        self.b =b
    def sub(self):
        return self.a-self.b
Sub = Math1(2,3)
result = Sub.sub()
print(result)

class BankAccount:
    def __init__(self , name , balance):
        self.name = name
        self.balance = balance
    def deposit(self , deposit):
        self.balance = self.balance + deposit
    def withdraw(self , amount):
        if amount > self.balance:
            print("Invalid transcation:")
        else:
            self.balance = self.balance - amount
    def show_balance(self):
        print("current balance is : ", self.balance)
acc = BankAccount("chandu",40000)
acc.deposit(30000)
acc.withdraw(10000)
acc.show_balance()

import json
d = {
    "name":"chandrakiran",
    "phno":984894948
}
with open("data.json","w") as f:
    json.dump(d,f)
# json.dump is used to  write to json to file.