import sqlite3
from os import getcwd

"""
# ?    Function that creates the DB
"""


def data_base():
    # Get current directory to store the db file in the correct folder
    pwd = getcwd()
    connection = sqlite3.connect(f"{pwd}/src/db/data_base.db")

    try:
        conn = sqlite3.connect(f"{pwd}/src/db/data_base.db")
        # Create the cursor to execute the table creation sentences
        cursor = connection.cursor()
        cursor.execute(
            """
			  create table if not exists passwords (
				  passwd_id integer primary key autoincrement,
				  passwd text not null,
				  description text,
				  creation_date text
			  )
		  """
        )

        cursor.execute(
            """
			  create table if not exists pin (
				  pin_id integer primary key autoincrement,
				  pin integer not null,
				  description text,
				  creation_date text
			  )
		  """
        )
        conn.commit()

    # If an sql error happens:
    except sqlite3.Error as e:
        print(e)

    return connection


class Password:
    def __init__(self):
        self.__conn = data_base()

    def insert_passwd(self, new_passwd, descr, date):
        cur = self.__conn.cursor()
        try:
            sentence = f"INSERT INTO passwords('passwd','description','creation_date') VALUES (?,?,?)"
            cur.execute(sentence, [new_passwd, descr, date])
            self.__conn.commit()
        except sqlite3.Error as e:
            print(e)
