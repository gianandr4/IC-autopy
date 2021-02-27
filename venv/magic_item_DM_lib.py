import pyodbc
#import win32api
import pyodbc
import sys
import datetime

try:
    #ip or hostname
    ip = 'IC-Project'
    username = r'administrator'
    password = 'Qwerty123!'



    conn = pyodbc.connect('Driver={ODBC Driver 11 for SQL Server};'
                          'Server=IC-PROJECT;'
                          'UID=autopy;'
                          r'PWD=pyauto111;'
                          'DATABASE=IC-Project;'
                          )

    cursor = conn.cursor()





    select_record = '''SELECT * FROM T_Items'''
    cursor.execute(select_record)

    for row in cursor:
        print(row)

    # delete_query = '''DELETE FROM T_Items WHERE Item_Price=125'''
    # cursor.execute(delete_query )
    # conn.commit()


    # update_query = ''' UPDATE T_Items SET Item_Price = 400 WHERE Item_Name='Peos' '''
    # cursor.execute(update_query)
    # conn.commit()


    #################################################################

    # name = "Peos"
    # price = 125
    # ccy = 'gp'
    # dti = datetime.datetime.now()
    #
    # insert_records = '''INSERT INTO T_Items (Item_Name,Item_Price,Item_CCY,DTInsert) VALUES(?,?,?,?) '''
    # cursor.execute(insert_records, name, price, ccy, dti)
    # conn.commit()
    #
    # item_Name
    # Item_Price
    # Item_CCY
    # DTInsert
    #
    # insert_records = '''INSERT INTO Books(Item_Name, Item_Price, Item_CCY, DTInsert) VALUES(?,?) '''
    # cursor.execute(insert_records, name, price)
    # conn.commit()
    #
    #

########################################

    input('New table')
    for row in cursor:
        print(row)
except:
    print(sys.exc_info())


# USE LibraryDB
# CREATE TABLE Books
# (
# Id INT PRIMARY KEY IDENTITY(1,1),
# Name VARCHAR (50) NOT NULL,
# Price INT
# )
#
#
# ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  CONNECT TO DB
# import pyodbc
# conn = pyodbc.connect('Driver={SQL Server};'
#                       'Server=DESKTOP-IIBLKH1\SQLEXPRESS;'
#                       'Database=LibraryDB;'
#                       'Trusted_Connection=yes;')
#
#
# ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  INSERT SINGLE RECORD
# name = "Book - A"
# price = 125
#
# insert_records = '''INSERT INTO Books(Name, Price) VALUES(?,?) '''
# cursor.execute(insert_records, name, price)
# conn.commit()
#
#
# ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  INSERT MULTIPLE RECORDS
# record_1 = ["Book - B", 300]
# record_2 = ["Book - C", 200]
#
# record_list = []
# record_list.append(record_1)
# record_list.append(record_2)
#
# insert_records = '''INSERT INTO Books(Name, Price) VALUES(?,?) '''
# cursor.executemany(insert_records, record_list)
# conn.commit()
#
# ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  SELECT RECORDS
# select_record = '''SELECT * FROM Books'''
# cursor.execute(select_record)
#
# for row in cursor:
#     print(row)
#
# ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  UPDATE RECORDS
# update_query = '''UPDATE Books SET Price = 400 WHERE Id= 1'''
# cursor.execute(update_query)
# conn.commit()
#
#
# ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  DELETE RECORDS
# delete_query = '''DELETE FROM Books WHERE Id= 1'''
# cursor.execute(delete_query )
# conn.commit()
#
#



