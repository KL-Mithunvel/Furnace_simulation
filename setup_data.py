
import mysql.connector as mysql
import sqlite3 as sql
con = sql.connect('coco.db')

cur = con.cursor()
if cur:
    print('connected')
else:
    print('not connected')
#cur.execute('create table shc (sno ,name, heat_cepacity)')
#cur.execute('create table shc (sno ,name, heat_cepacity)')


def create_tables():
    if not check_if_tables_exist('settings'):
        # create table
        pass


def check_if_tables_exist(tab):
    # check if table exists
    print('Check if STUDENT table exists in the database:')
    list_of_tables = cur.execute(
     f"""SELECT tableName FROM sqlite_master WHERE type='table'
      AND tableName='{tab}'; """).fetchall()

    return True if list_of_tables else False
