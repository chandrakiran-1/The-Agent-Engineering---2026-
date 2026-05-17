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