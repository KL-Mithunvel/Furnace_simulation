import sqlite3 as sql
import mysql.connector as mysql
con = sql.connect('coco.db')

cur = con.cursor()
if cur:
    print('connected')
else:
    print('not connected')
#cur.execute('create table SHC (sno int primary key,Name varchar(255) ,Heatcepacity int not null)')
con.execute("INSERT INTO TABLE SHC  VALUES(1,coal,25000 )")
#cur.execute('select * from SHC')


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
