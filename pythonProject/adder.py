import sqlite3 as sq3

TABLENAME = 'prices'


def create_table(name=TABLENAME):
    with sq3.connect("test_database.db") as connection:
        cursor = connection.cursor()
        query = """CREATE TABLE IF NOT EXISTS {}
                    (id integer primary key autoincrement,
                    name text, 
                    open_price real,
                    low_price real,
                    high_price real,
                    last_price real, 
                    updatetime text,
                    systime text);""".format(name)
        cursor.execute(query)


def insert_into_table(info, name=TABLENAME):
    with sq3.connect("test_database.db") as connection:
        cursor = connection.cursor()
        query = """INSERT INTO {} (name, open_price, low_price, high_price, last_price, updatetime, systime) VALUES
            {};""".format(name, info)
        cursor.execute(query)


def select_info_from_table(name=TABLENAME):
    with sq3.connect("test_database.db") as connection:
        cursor = connection.cursor()
        query = """SELECT * FROM {};""".format(name)
        return cursor.execute(query).fetchall()


def rows_count_from_table(name=TABLENAME):
    with sq3.connect("test_database.db") as connection:
        cursor = connection.cursor()
        query = """SELECT count(*) from {};""".format(name)
        return cursor.execute(query).fetchone()
