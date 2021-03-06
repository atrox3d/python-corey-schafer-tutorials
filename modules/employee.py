"""
https://www.youtube.com/watch?v=pd-0G0MigUA
"""

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
    """a sample DAO"""

    def __init__(self, dbname=':memory:'):
        """construct DAO obj and creates db"""
        self.dbname = dbname
        self.conn = None
        self.cursor = None
        self.memorydb = True if dbname == ':memory:' else False

        self._setup()

    def _setup(self):
        """creates db"""
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
        """checks if connection is open"""
        if self.conn is not None:
            try:
                print('connection status...', end='')
                resultset = self.conn.execute("SELECT 1 FROM sqlite_master LIMIT 1;")
                print('open')
                return True
            except sqlite3.ProgrammingError as e:
                print('closed')
                return False
        else:
            return False

    def open(self):
        """opens connection"""
        try:
            print(f'{"open":<20}| connecting to db: {self.dbname}...', end='')
            self.conn = sqlite3.connect(self.dbname)
            self.cursor = self.conn.cursor()
            print("ok")
            return True
        except sqlite3.OperationalError as oe:
            print(oe)
            return False

    def close(self):
        """closes connection"""
        print(f'{"close":<20}| closing connection')
        self.conn.close()

    def query(self, sql, **kwargs):
        """generalized query"""
        print(f'{"query":<20}| isopen...', end='')
        if not self.isopen():
            print('closed')
            print(f'{"query":<20}| open...')
            if not self.open():
                print(f'{"query":<20}| ERROR, cannot connect')
        else:
            print('ok')

        with self.conn:
            try:
                for sqlline in sql.split('\n'):
                    print(f'{"query":<20}| executing: {sqlline}')
                print(f'{"query":<20}| with args {kwargs}')

                result = self.cursor.execute(sql, kwargs)
            except sqlite3.OperationalError as oe:
                # if self.memorydb:
                #     self.close()
                print(f'{"query":<20}| ERROR: {oe}')
                result = False

        if not self.memorydb:
            print(f'{"query":<20}| closing connection')
            self.close()
        else:
            print(f'{"query":<20}| db is in memory, keeping connection open')

        return result

    def save(self, emp):
        """saves Employee on db"""
        sql = """
            INSERT INTO employees 
            VALUES(
                :first,
                :last,
                :pay
            )
            """

        return self.query(
            sql,
            first=emp.first,
            last=emp.last,
            pay=emp.pay
        )

    def update(self, emp, pay=None):
        """updates pay of Employee"""
        sql = """
            UPDATE employees
            SET pay = :pay
            WHERE first = :first AND last = :last
            """

        if pay is None:
            pay = emp.pay

        return self.query(
            sql,
            first=emp.first,
            last=emp.last,
            pay=pay
        )

    def delete(self, emp):
        """deletes Employee from db"""
        sql = """
            DELETE from employees
            WHERE first = :first AND last = :last
            """

        return self.query(
            sql,
            first=emp.first,
            last=emp.last
        )

    def list(self):
        """lists all Employees"""
        sql = "SELECT * FROM employees"
        return self.query(sql)

    def count(self):
        """counts all Employees"""
        sql = "SELECT COUNT(*) FROM employees"
        count = self.query(sql).fetchone()
        return count[0]


if __name__ == '__main__':
    print('main')
    dao = EmployeeDAO()
    emp1 = Employee('rob', 'lomb', 2000)

    dao.save(emp1)
    print(dao.list().fetchall())

    dao.update(emp1, 5000000)
    print(dao.list().fetchall())

    emp1.pay = 1
    dao.update(emp1)
    print(dao.list().fetchall())

    emp2 = Employee('pask', 'sin', 2000)
    dao.save(emp2)
    print(dao.list().fetchall())

    print(dao.count())

    dao.delete(emp1)
    print(dao.list().fetchall())

    print(dao.count())

    dao.close()
