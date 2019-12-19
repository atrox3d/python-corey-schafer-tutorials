from modules import utils


class Employee:
    raise_amount = 1.04
    count = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        # self.email = f'{first}.{last}@company.com'

        Employee.count += 1

    def fullname(self):
        return f'{self.first} {self.last}'

    def email(self):
        """
        initializing the email in the constructor causes the email

        to be out of sync when we change .first or .last

        so we created a method that always returns the correct value.

        although, when we use it. we must add parenthesis at the end .email()
        """
        return f'{self.first}.{self.last}@email.com'


utils.banner(
    'https://www.youtube.com/watch?v=jCzT9XFZ5bw',
    'getters, setters and deleters'
)

emp1 = Employee('bob', 'red', 5000)

emp1.first = 'Jim'

print(emp1.first)
print(emp1.email)
print(emp1.fullname())

