import sqlite3
from modules import utils

DBNAME = 'employee.db'
# conn = sqlite3.connect(':memory:')
conn = sqlite3.connect(utils.getdatafilepath(DBNAME))

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

cursor.execute(
    """
    INSERT INTO employees 
    VALUES(
        'corey',
        'schafer',
        50000
    )
    """)
conn.commit()
conn.close()
