import sqlite3


class Employee:
    """A sample Employee class"""

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)


class EmployeeDAO:
    def __init__(self, dbname=':memory:'):
        self.dbname = dbname

    def isopen(self):
        pass

    def open(self):
        pass

    def close(self):
        pass

    def query(self, query):
        pass

    def save(self, emp):
        pass

    def update(self, emp):
        pass

    def delete(self, emp):
        pass

    def get(self, emp):
        pass
