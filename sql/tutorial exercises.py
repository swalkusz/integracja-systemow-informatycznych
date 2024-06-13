import sqlite3
import sys
import pandas as pd
from datetime import date


def path_to_database():
    return "sql-tutorial/db/contact_tracing.db"

db_path = path_to_database()

def sql_query():
    return """select * from person;"""


def querying_from_python():
    connection = sqlite3.connect(db_path)
    cursor = connection.execute(sql_query())
    rows = cursor.fetchall()
    print(rows)


def incremental_fetch():
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    cursor = cursor.execute(sql_query())
    while row := cursor.fetchone():
        print(row)


def insert_delete():
    connection = sqlite3.connect(":memory:")
    cursor = connection.cursor()
    cursor.execute("create table example(num integer);")

    cursor.execute("insert into example values (10), (20);")
    print("after insertion", cursor.execute("select * from example;").fetchall())

    cursor.execute("delete from example where num < 15;")
    print("after deletion", cursor.execute("select * from example;").fetchall())


def interpolating_values():
    connection = sqlite3.connect(":memory:")
    cursor = connection.cursor()
    cursor.execute("create table example(num integer);")

    cursor.executemany("insert into example values (?);", [(10,), (20,)])
    print("after insertion", cursor.execute("select * from example;").fetchall())


def script_execution():
    SETUP = """\
    drop table if exists example;
    create table example(num integer);
    insert into example values (10), (20);
    """

    connection = sqlite3.connect(":memory:")
    cursor = connection.cursor()
    cursor.executescript(SETUP)
    print("after insertion", cursor.execute("select * from example;").fetchall())


def sqlite_exceptions():
    SETUP = """\
    create table example(num integer check(num > 0));
    insert into example values (10);
    insert into example values (-1);
    insert into example values (20);
    """

    connection = sqlite3.connect(":memory:")
    cursor = connection.cursor()
    try:
        cursor.executescript(SETUP)
    except sqlite3.Error as exc:
        print(f"SQLite exception: {exc}")
    print("after execution", cursor.execute("select * from example;").fetchall())


def python_in_sqlite():
    SETUP = """\
    create table example(num integer);
    insert into example values (-10), (10), (20), (30);
    """

    def clip(value):
        if value < 0:
            return 0
        if value > 20:
            return 20
        return value

    connection = sqlite3.connect(":memory:")
    connection.create_function("clip", 1, clip)
    cursor = connection.cursor()
    cursor.executescript(SETUP)
    for row in cursor.execute("select num, clip(num) from example;").fetchall():
        print(row)


def handling_dates_and_times():
    # Convert date to ISO-formatted string when writing to database
    def _adapt_date_iso(val):
        return val.isoformat()
    sqlite3.register_adapter(date, _adapt_date_iso)

    # Convert ISO-formatted string to date when reading from database
    def _convert_date(val):
        return date.fromisoformat(val.decode())
    sqlite3.register_converter("date", _convert_date)

    SETUP = """\
    create table events(
        happened date not null,
        description text not null
    );
    """

    connection = sqlite3.connect(":memory:", detect_types=sqlite3.PARSE_DECLTYPES)
    cursor = connection.cursor()
    cursor.execute(SETUP)

    cursor.executemany(
        "insert into events values (?, ?);",
        [(date(2024, 1, 10), "started tutorial"), (date(2024, 1, 29), "finished tutorial")],
    )
    for row in cursor.execute("select * from events;").fetchall():
        print(row)


def pandas_and_sql():
    connection = sqlite3.connect(db_path)
    df = pd.read_sql(sql_query(), connection)
    print(df)



def create_sqlite_database(filename):
    """ create a database connection to an SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(filename)
        print(sqlite3.sqlite_version)
    except sqlite3.Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

# create_sqlite_database("my.db")
