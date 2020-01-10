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
        self.conn = None
        self.cursor = None

    def isopen(self):
        try:
            print('connection status...', end='')
            resultset = self.conn.execute("SELECT 1 FROM sqlite_master LIMIT 1;")
            print('open')
            return True
        except sqlite3.ProgrammingError as e:
            print('closed')
            return False

    def open(self):
        try:
            print(f'connecting to db {self.dbname}...')
            self.conn = sqlite3.connect(self.dbname)
            self.cursor = self.conn.cursor()
        except sqlite3.OperationalError as oe:
            print(oe)

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
