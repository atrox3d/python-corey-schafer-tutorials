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
        #
        #   if self.raise_amount is not defined into the current instance
        #   this will use the class variable
        #   else it will use the instance variable
        #
        self.pay = int(self.pay * self.raise_amount)

    def print_salary(self):
        print(f'{self.fullname()}: pay={self.pay}, raise amount={self.raise_amount} | dict= {self.__dict__}')

    @classmethod
    def set_raiseamount(cls, amount):
        cls.raise_amount = amount


emp1 = Employee('bob', 'red', 5000)
emp2 = Employee('kate', 'blue', 5500)

utils.banner('print salaries before class method')
emp1.print_salary()
emp2.print_salary()

Employee.set_raiseamount(2)                                 # change class variable

utils.banner('print salaries after class method')
emp1.print_salary()
emp2.print_salary()

emp1.set_raiseamount(3)                                     # change class variable

utils.banner('print salaries after class method from instance')
emp1.print_salary()
emp2.print_salary()
