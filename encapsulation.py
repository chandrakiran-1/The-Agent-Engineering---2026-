class Bank:
    def __init__(self):
        self.__balance = 10000
    def deposit(self , amount):
        self.__balance = self.__balance + amount
    def show_balance(self ):
        print("balance : ", self.__balance)
b = Bank()
b.deposit(1200)
b.show_balance()

class Demo:
    def __len__(self):
        return 6
d = Demo()
print(len(d))

class String:
    def __str__(self):
        return " this is a sentence:"
s = String()
print(s)

class Constructor:
    def __init__(self , name):
        self.name = name
    def display(self):
        return self.name
c  = Constructor("chandu")
res = c.display()
print(res)
