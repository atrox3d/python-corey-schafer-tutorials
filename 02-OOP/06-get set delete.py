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

    #
    # getter
    #
    @property
    def fullname(self):
        """
        combines first<space>last

        :return: fullname
        """
        return f'{self.first} {self.last}'

    #
    # setter
    #
    @fullname.setter
    def fullname(self, name):
        """
        split full name by <space>

        assigns the result to first and last

        :param name:
        """
        self.first, self.last = name.split(' ')

    #
    # deleter
    #
    @fullname.deleter
    def fullname(self):
        """
        deletes both first and last
        """
        self.first = None
        self.last = None

    #
    # only getter
    #
    @property
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

utils.banner('change name from bob to Jim')
emp1.first = 'Jim'
print(emp1.first)
print(emp1.email)
print(emp1.fullname)

utils.banner('change fullname to rob robbins')
emp1.fullname = 'rob robbins'
print(emp1.first)
print(emp1.email)
print(emp1.fullname)

utils.banner('del fullname')
del emp1.fullname
print(emp1.first)
print(emp1.email)
print(emp1.fullname)
