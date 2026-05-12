class Employee:
    def __init__(self , frist , last , pay):
        self.frist = frist
        self.last = last
        self.pay = pay
        self.email = f"{frist.lower()}.{last.lower()}@infosys.com"
    def Full_name(self):
        return f"{self.frist} {self.last}"
    def Increase_pay(self , percent):
        self.pay = int(self.pay * (1 + percent/100))

emp1 = Employee("Chandu", "reddy" , 60000)
emp2 = Employee("Sharma", "kapoor", 50000)


print(emp1.__dict__)
print(emp2.__dict__)
print(emp1.pay)
emp1.Increase_pay(5)
print(emp1.pay)

Employee.Increase_pay(emp1 , 7)
print(emp1.pay)