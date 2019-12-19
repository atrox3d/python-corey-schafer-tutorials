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
        print(
            f'{self.__class__.__name__:<10} | '
            f'{self.fullname():<10}: pay={self.pay}, raise amount={self.raise_amount!s:>4} | '
            f'dict= {self.__dict__}'
        )

    @classmethod
    def from_string(cls, emp_str, sep=';'):
        first, last, pay = emp_str.split(sep)
        emp = cls(first, last, pay)
        return emp

    def __repr__(self):
        #
        #   __str__ falls back to __repr__
        #
        return f'Employee({self.first!r}, {self.last!r}, {self.pay!r})'

    def __str__(self):
        return f'{self.fullname()}, {self.email}'

    # synonim
    __STR__ = __str__

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())


utils.banner('magic methods')
emp1 = Employee('bob', 'red', 5000)
