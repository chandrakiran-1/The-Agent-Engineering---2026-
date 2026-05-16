class Employee:
    company = " infosys"
    def __init__(self , name):
        self.name = name
    @classmethod
    def Change_company(cls , new_company):
        cls.company = new_company
print(Employee.company)
Employee.Change_company("microsoft")
print(Employee.company)