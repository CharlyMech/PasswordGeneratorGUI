import sqlite3
from os import getcwd

'''
# ?    Function that creates the DB
'''


def data_base():
    # Get current directory to store the db file in the correct folder
    pwd = getcwd()
    connection = sqlite3.connect(f"{pwd}/src/db/data_base.db")

    try:
        conn = sqlite3.connect(f"{pwd}/src/db/data_base.db")
        # Create the cursor to execute the table creation sentences
        cursor = connection.cursor()
        cursor.execute("""
			  create table if not exists passwords (
				  passwd_id integer primary key autoincrement,
				  passwd text not null,
				  description text,
				  creation_date text
			  )
		  """)

        cursor.execute("""
			  create table if not exists pin (
				  pin_id integer primary key autoincrement,
				  pin integer not null,
				  description text,
				  creation_date text
			  )
		  """)
        conn.commit()

    # If an sql error happens:
    except sqlite3.Error as e:
        print(e)


# class Password():
#     def __init__(self):
#         super().__init__(__directory)
#         try:
#             self.__connection = sqlite3.connect(
#                 f"{self.__directory}/src/db/data_base")
#             self.__cursor = self.__connection.cursor()
#         except sqlite3.Error as e:
#             print(e)

#     def passwd_insert(self, password, descr):
#         data = [password, descr]
#         try:
#             sql = '''INSERT INTO passwords(passwd, description, creation_date) VALUES (?,?,(SELECT strftime('%d/%m/%Y', 'now')))'''
#             sql_exec = self.__cursor.execute(sql, data)
#             self.__connection.commit()
#             self.__cursor.close()
#         except sqlite3.Error as e:
#             print(e)

#     # def passwd_update(self, passwd_id):
#     #     data = [password, descr]
#     #     try:
#     #         sql = '''INSERT INTO passwords(passwd, description, creation_date) VALUES (?,?,(SELECT strftime('%d/%m/%Y', 'now')))'''
#     #         sql_exec = self.__cursor.execute(sql, data)
#     #         self.__connection.commit()
#     #         self.__cursor.close()
#     #     except sqlite3.Error as e:
#     #         print(e)

#     def passwd_delete(self, passw_id):
#         try:
#             sql = '''DELETE FROM passwords WHERE passwd_id = ?'''
#             sql_exec = self.__cursor.execute(sql, passw_id)
#             self.__connection.commit()
#         except sqlite3.Error as e:
#             print(e)
#         finally:
#             self.__cursor.close()

#     def passwd_select(self, passw_id):
#         try:
#             sql = '''SELECT * FROM passwords WHERE passwd_id = ?'''
#             sql_exec = self.__cursor.execute(sql, passw_id)
#             self.__connection.commit()
#         except sqlite3.Error as e:
#             print(e)
#         finally:
#             self.__cursor.close()

#     def passwd_select_all(self):
#         try:
#             sql = '''SELECT * FROM passwords'''
#             sql_exec = self.__cursor.execute(sql)
#             self.__connection.commit()
#             select = self.__cursor.fetchall()
#             return select
#         except sqlite3.Error as e:
#             print(e)
#         finally:
#             self.__cursor.close()


# obj = Password()
# obj.passwd_insert('testeo1', '')

# # obj.passwd_select(3)
