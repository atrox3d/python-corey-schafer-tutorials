from modules import utils


class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f'{first}.{last}@company.com'

    def fullname(self):
        return f'{self.first}, {self.last}'


emp1 = Employee('bob', 'red', 5000)
emp2 = Employee('kate', 'blue', 5500)

print(emp1.fullname())
print(Employee.fullname(emp1))
