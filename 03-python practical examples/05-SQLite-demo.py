import sqlite3
from modules import utils
from modules.employee import Employee


DBMEMORY = True

if DBMEMORY:
    DBNAME = ':memory:'
    DBPATH = ':memory:'
else:
    DBNAME = 'employee.db'
    DBPATH = utils.getdatafilepath(DBNAME)

conn = sqlite3.connect(DBPATH)
cursor = conn.cursor()

try:
    cursor.execute("DROP TABLE IF EXISTS employees")
    cursor.execute(
        """
        CREATE TABLE employees (
            first text,
            last text,
            pay integer
        )
        """
    )
except sqlite3.OperationalError as oe:
    print(oe)
    exit()

# cursor.execute("SELECT COUNT (*) FROM employees")
# count = cursor.fetchall()
# count = cursor.fetcmany()
# count = cursor.fetchone()
# print(type(count))
# print(*count)
# exit()

emp1 = Employee('john', 'doe', 80000)
emp2 = Employee('jane', 'doe', 90000)

print(emp1.fullname)

cursor.execute(
    """
    INSERT INTO employees 
    VALUES(
        'corey',
        'schafer',
        50000
    )
    """
)
conn.commit()
cursor.execute(
    """
    INSERT INTO employees 
    VALUES(
        'mary',
        'schafer',
        50000
    )
    """
)
conn.commit()

cursor.execute("SELECT COUNT (*) FROM employees")
count = cursor.fetchone()
print(*count)

cursor.execute(
    """
    SELECT * FROM employees
    WHERE last= 'schafer'
    """
)
record = cursor.fetchone()
print(record)
print(*record)

cursor.execute(
    """
    SELECT * FROM employees
    WHERE last= 'schafer'
    """
)
records = cursor.fetchall()
print(records)
print(*records)

conn.commit()
conn.close()
