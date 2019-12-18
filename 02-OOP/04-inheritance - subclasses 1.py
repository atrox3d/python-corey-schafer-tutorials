from modules import utils


class Employee:
    raise_amount = 1.04
    count = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f'{first}.{last}@company.com'

        Employee.count += 1

    def fullname(self):
        return f'{self.first}, {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    def print_salary(self):
        print(f'{self.fullname()}: pay={self.pay}, raise amount={self.raise_amount} | dict= {self.__dict__}')

    @classmethod
    def from_string(cls, emp_str, sep=';'):
        first, last, pay = emp_str.split(sep)
        emp = cls(first, last, pay)
        return emp


class Developer(Employee):
    pass


emp1 = Developer.from_string('bob;red;5000')
emp2 = Developer.from_string('kate;blue;5500')


emp1.print_salary()
emp2.print_salary()

print(help(Developer))
