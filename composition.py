
#------------composition---------------------------------
class Salary:
    def __init__(self, pay, bonus):
        self.pay=pay
        self.bonus=bonus

    def annual_salary(self):
        return print(f"total salary is:{(self.pay*12)+ self.bonus} ")

class Employee:
    def __init__(self, name, age, pay, bonus):
        self.name=name
        self.age=age
        self.salary_obj=Salary(pay, bonus)

    def total_salary(self):
        self.salary_obj.annual_salary()

emp1=Employee("Harry", 24, 200000, 10000)
emp1.total_salary()


#--------------------aggregation------------------


class Salary:
    def __init__(self, pay, bonus):
        self.pay=pay
        self.bonus=bonus

    def annual_salary(self):
        #return print(f"total salary is:{(self.pay*12)+ self.bonus} ")
        print(f"this is total salary is:{(self.pay*12)+ self.bonus} ")

class Employee:
    def __init__(self, name, age, salary):
        self.name=name
        self.age=age
        self.salary_obj=salary

    def total_salary(self):
        self.salary_obj.annual_salary()

salary4emp1=Salary(100000, 20000)
emp1=Employee("Harry", 24, salary4emp1)
emp1.total_salary()