import sqlite3
from os import getcwd


def data_base():
    connection = None
    pwd = getcwd()
    print(pwd)
    try:
        connection = sqlite3.connect(f"{pwd}/data_base.db")
        # connection = sqlite3.connect(f"{pwd}/src/db/data_base.db") -> This is the good one
        print(sqlite3.version)
        print("La base de datos ha sido creada")

        connection.execute("""
			  create table if not exists passwords (
				  passwd_id integer primary key autoincrement,
				  passwd text not null,
				  description text,
				  creation_date text
			  )
		  """)

        connection.execute("""
			  create table if not exists pin (
				  pin_id integer primary key autoincrement,
				  pin integer not null,
				  description text,
				  creation_date text
			  )
		  """)
    except sqlite3.Error as e:
        print(e)
    finally:
        if connection:
            connection.close()


data_base()


# conn = sqlite3.connect('data_base.db')
# sql_insertion = "INSERT INTO passwords(passwd, description, creation_date) VALUES('passwd-test-3',NULL,NULL)"
# cur = conn.cursor()
# cur.execute(sql_insertion)
# conn.commit()
