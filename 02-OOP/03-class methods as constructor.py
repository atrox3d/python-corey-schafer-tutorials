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

    @classmethod
    def from_string(cls, emp_str, sep=';'):
        first, last, pay = emp_str.split(sep)
        # emp = cls(first, last, pay)
        emp = cls(*emp_str.split(sep))          # use unpacking
        return emp


emp1 = Employee.from_string('bob;red;5000')
emp2 = Employee.from_string('kate;blue;5500')


emp1.print_salary()
emp2.print_salary()

