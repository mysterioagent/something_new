import sqlite3 as sq3

TABLENAME = 'prices'


def drop_table(name=TABLENAME):
    with sq3.connect("test_database.db") as connection:
        cursor = connection.cursor()
        query = """drop table if exists {};""".format(name)
        cursor.execute(query)

def delete_upper_rows(name=TABLENAME):
    with sq3.connect("test_database.db") as connection:
        cursor = connection.cursor()
        query = """delete from {} where name||id||date(systime) 
                    in (select name||id||dt from 
                    (select name, id as id, date(systime) as dt,
                    row_number() over (partition by name, date(systime) order by datetime(systime) desc) as rn
                    from {}) r 
                    where rn > 1);""".format(name, name)
        cursor.execute(query)



