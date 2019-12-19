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


utils.banner(
    'https://www.youtube.com/watch?v=jCzT9XFZ5bw',
    'getters, setters and deleters'
)
emp1 = Employee('bob', 'red', 5000)
