from modules import utils


class Employee:
    #
    #   this is a class variable:
    #       visible from the class itslef:
    #                                       Employee.raise_amount
    #       visible from instances:
    #                                       emp1.raise_amount
    #                                       self.raise_amount
    #
    #   it can be overridden by defining the same name defined into a single instance
    #
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f'{first}.{last}@company.com'

    def fullname(self):
        return f'{self.first}, {self.last}'

    def apply_raise(self):
        #
        #   if self.raise_amount is not defined into the current instance
        #   this will use the class variable
        #   else it will use the instance variable
        #
        self.pay = int(self.pay * self.raise_amount)

    def print_salary(self):
        print(f'{self.fullname()}: pay={self.pay}, raise amount={self.raise_amount}')


emp1 = Employee('bob', 'red', 5000)
emp2 = Employee('kate', 'blue', 5500)
utils.banner('print salaries')
emp1.print_salary()
emp2.print_salary()
#
#   change class variable
#
utils.banner('change Employee.raise_amount', 'print salaries')
Employee.raise_amount = 1.05
emp1.print_salary()
emp2.print_salary()
print()
#
#   change instance variable of emp1,
#       - overrides class variable
#       - creates new property insto emp1 instance
#
utils.banner('change emp1.raise_amount', 'print salaries')
emp1.raise_amount = 1.06
emp1.print_salary()
emp2.print_salary()
print()
#
#   change again class variable
#   emp1.raise_amount is not affected anymore
#
utils.banner('change again Employee.raise_amount', 'print salaries')
Employee.raise_amount = 2
emp1.print_salary()
emp2.print_salary()
print()
