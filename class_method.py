class BankAccount:
    def __init__(self, bank_holder , balance):
        self.bank_holder = bank_holder
        self.balance = balance
    def deposit(self , deposit):
        self.balance = self.balance + deposit
    def withdraw(self , money):
        if money <0:
            print("Invalid amount")
        elif money <= self.balance:
            self.balance = self.balance - money
        else:
            print("insufficient balane: ")
    def display(self):
        print("holder :",self.bank_holder)
        print("balance :",self.balance)
    @classmethod
    def from_String(cls , data):
        bank_holder , balance = data.split("-")
        return cls(bank_holder , int(balance))
acc = BankAccount.from_String("chandu-100000")
acc.deposit(5000)
acc.withdraw(20000)
acc.display()
