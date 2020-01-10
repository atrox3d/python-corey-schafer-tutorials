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

        self._setup()

    def _setup(self):
        if self.query(
            """
            CREATE TABLE IF NOT EXISTS employees
            (
                first text,
                last text,
                pay integer
            )
            """
        ):
            return True
        else:
            return False

    def isopen(self):
        if self.conn is not None:
            try:
                print('connection status...', end='')
                resultset = self.conn.execute("SELECT 1 FROM sqlite_master LIMIT 1;")
                print('open')
                return True
            except sqlite3.ProgrammingError as e:
                print('closed')
                return False

        return False

    def open(self):
        try:
            print(f'connecting to db {self.dbname}...')
            self.conn = sqlite3.connect(self.dbname)
            self.cursor = self.conn.cursor()
            return True
        except sqlite3.OperationalError as oe:
            print(oe)
            return False

    def close(self):
        self.conn.close()

    def query(self, query, **kwargs):
        if not self.isopen():
            if self.open():
                with self.conn:
                    try:
                        print(f'executing "{query}" with args {kwargs}')
                        result = self.cursor.execute(query, **kwargs)
                        return result
                    except sqlite3.OperationalError as oe:
                        print(oe)

    def save(self, emp):
        pass

    def update(self, emp):
        pass

    def delete(self, emp):
        pass

    def get(self, emp):
        pass


if __name__ == '__main__':
    print('main')
    dao = EmployeeDAO()
