import sqlite3
from modules import utils
from modules.employee import Employee


DBMEMORY = True
#
#   set db variables
#
if DBMEMORY:
    DBNAME = ':memory:'
    DBPATH = ':memory:'
else:
    DBNAME = 'employee.db'
    DBPATH = utils.getdatafilepath(DBNAME)
#
#   connect to db
#
try:
    print(f'connecting to db {DBPATH}...')
    conn = sqlite3.connect(DBPATH)
except sqlite3.OperationalError as oe:
    print(oe)
    exit(1)
#
#   check connection
#
try:
    print('connection status...', end='')
    resultset = conn.execute("SELECT 1 FROM sqlite_master LIMIT 1;")
    print('open')
except sqlite3.ProgrammingError as e:
    print('closed')
#
#   get cursor
#
cursor = conn.cursor()
#
#   setup db, deterministic
#
with conn:
    try:
        print('dropping table employees if already existing...', end='')
        cursor.execute("DROP TABLE IF EXISTS employees")
        print('ok')

        print('creating table employees...', end='')
        cursor.execute(
            """
            CREATE TABLE employees (
                first text,
                last text,
                pay integer
            )
            """
        )
        print('ok')
    except sqlite3.OperationalError as oe:
        print(oe)
        conn.close()
        exit()

# cursor.execute("SELECT COUNT (*) FROM employees")
# count = cursor.fetchall()
# count = cursor.fetcmany()
# count = cursor.fetchone()
# print(type(count))
# print(*count)
# exit()

#
#   setup data
#
emp1 = Employee('john', 'doe', 80000)
emp2 = Employee('jane', 'doe', 90000)
print()
print('creating 2 employee objs')
print(f'emp1: {emp1.fullname}')
print(f'emp2: {emp2.fullname}')
print('emp1 dictionary: ', emp1.__dict__)
#
#   insert data
#
with conn:
    try:
        print()
        print('insert employees...', end='')
        cursor.execute(
            """
            INSERT INTO employees 
            VALUES(
                :first,
                :last,
                :pay
            )
            """,
            dict(
                    first=emp1.first,
                    last=emp1.last,
                    pay=emp1.pay
            )
        )

        cursor.execute(
            """
            INSERT INTO employees 
            VALUES(
                :first,
                :last,
                :pay
            )
            """,
            emp2.__dict__
        )
        print('ok')
    except sqlite3.OperationalError as oe:
        print(oe)
#
#   select data
#
cursor.execute("SELECT COUNT (*) FROM employees")
count = cursor.fetchone()
print(f'total employees: {count[0]}')

print()
print('select emp1')
cursor.execute(
    """
    SELECT * FROM employees
    WHERE first= :first
    """,
    dict(first=emp1.first)
)
record = cursor.fetchone()
print('record tuple   : ', record)
print('unpacked record: ', *record)

print()
print('select all employees')
cursor.execute(
    """
    SELECT * FROM employees
    -- WHERE last= 'schafer'
    """
)
records = cursor.fetchall()
print('records list         : ', records)
print('unpacked records list: ', *records)

print('closing connection')
conn.close()
conn.close()
conn.close()

print()
try:
    print('connection status...', end='')
    resultset = conn.execute("SELECT 1 FROM sqlite_master LIMIT 1;")
    print('open')
except sqlite3.ProgrammingError as e:
    print('closed')
