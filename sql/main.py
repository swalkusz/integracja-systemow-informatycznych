import sqlite3
from sqlite3 import Error

def create_connectrion(filename):
    conn = sqlite3.connect(filename)
    try:
        c = conn.cursor()
        c.execute(sql_query())
        headers = [description[0] for description in c.description]
        print(headers)
        for row in c.fetchall():
            print(row)
    except Error as e:
        print(e)
    conn.close()

def sql_query():
    return """
select * from job;
"""


if __name__ == '__main__':
    create_connectrion("sql-tutorial/db/penguins.db")
