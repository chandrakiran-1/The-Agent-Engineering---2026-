class Employee:

    raised_percentage= 1.04 # class variable
    count = 0

    __slots__ = ["frist" , "last" , "pay" ,"email"]

    def __init__(self , frist , last , pay):
        self.frist = frist
        self.last = last
        self.pay = pay
        self.email = f"{frist.lower()}.{last.lower()}@infosys.com"
        Employee.count+= 1
        
    def Full_name(self):
        return f"{self.frist} {self.last}"
    def Increase_pay(self):
        self.pay = int(self.pay * self.raised_percentage)

emp1 = Employee("Chandu", "reddy" , 60000)
emp2 = Employee("Sharma", "kapoor", 50000)





print(emp1.pay)

print(Employee.raised_percentage)

print(emp1.raised_percentage)
print(emp2.raised_percentage)
emp1.Increase_pay()
print(emp1.pay)

print(emp1.raised_percentage)
print(Employee.__dict__)
print(Employee.count)
print(emp1.count)