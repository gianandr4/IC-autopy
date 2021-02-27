import pyodbc
import win32api
import pyodbc
import sys
import datetime

database='IC-Project'
table='T_Items'


try:
    class CRUD_autopy():
        def __init__(self,name,price,ccy='gp'):
            self.Item_Name = '' ########## nonull
            self.Item_Special = ''
            self.Item_Price = int(1) ########## nonull int
            self.Item_CCY = 'gp/cp/pp' ########## nonull
            self.Item_Slot = ''
            self.Item_Casterlevel = ''
            self.Item_Aura = ''
            self.Item_Weight = ''
            self.Item_Description = ''
            self.Item_Craftprerequisites = ''
            self.Item_Costtocreate = ''
            self.Item_Lore = ''
            self.Item_BookNametem_BookName = ''
            self.Item_BookDisplay = ''
            self.DTInsert = datetime.datetime.now()
            self.Note = ''
            self.Item_Activation = ''

    def connect(): # CONNECT TO DATABASE, AND RETURN CURSOR
        conn = pyodbc.connect('Driver={ODBC Driver 11 for SQL Server};'
                              'Server=IC-PROJECT;'
                              'UID=autopy;'
                              r'PWD=pyauto111;'
                              'DATABASE=IC-Project;'
                              )
        print('Connection to',database,'successful')
        return conn.cursor()


    # def create_table():
    #     return


    def read_convert(table,to_pandas=False):
        cursor=connect()

        select_record = '''SELECT * FROM '''+table
        cursor.execute(select_record)
        out=[]

        for row in cursor:
            print(row)
            out.append(row)

        if topandas:
            try:
                import pandas
                out=pandas.DataFrame(out)

            except:
                print(sys.exc_info(),'Could not conver to pandas, list is returned')
        return out



    def list_write(input, frompandas=False):
        # name = "Peos"
        # price = 125
        # ccy = 'gp'
        # dti = datetime.datetime.now()

        insert_records = '''INSERT INTO '''+table+''' (Item_Name,Item_Price,Item_CCY,DTInsert) VALUES(?,?,?,?) '''
        cursor.execute(insert_records, name, price, ccy, dti)
        conn.commit()
        return



    def delete_entry():
        return





    name = NULL
    special = ''
    price = ''
    ccy = ''
    slot = ''
    cl = ''
    aura = ''
    weight = ''
    desc = ''
    craft = ''
    cost = ''
    lore = ''
    bname = ''
    bdis = ''
    dti = ''
    note = ''
    act = ''
    x=CRUD_autopy(
        name,
        special,
        price,
        ccy,
        slot,
        cl,
        aura,
        weight,
        desc,
        craft,
        cost,
        lore,
        bname,
        bdis,
        dti,
        note,
        act,
                )





    # #ip or hostname
    # ip = 'IC-Project'
    # username = r'administrator'
    # password = 'Qwerty123!'
    #
    #
    #
    # conn = pyodbc.connect('Driver={ODBC Driver 11 for SQL Server};'
    #                       'Server=IC-PROJECT;'
    #                       'UID=autopy;'
    #                       r'PWD=pyauto111;'
    #                       'DATABASE=IC-Project;'
    #                       )
    #
    # cursor = conn.cursor()
    #
    #
    #
    #
    #
    # select_record = '''SELECT * FROM T_Items'''
    # cursor.execute(select_record)
    #
    # for row in cursor:
    #     print(row)

###############################################################################################
    # name = "Peos"
    # price = 125
    # ccy = 'gp'
    # dti = datetime.datetime.now()
    #
    # insert_records = '''INSERT INTO T_Items (Item_Name,Item_Price,Item_CCY,DTInsert) VALUES(?,?,?,?) '''
    # cursor.execute(insert_records, name, price, ccy, dti)
    # conn.commit()

    #item_Name
    #Item_Price
    #Item_CCY
    #DTInsert



    # insert_records = '''INSERT INTO Books(Item_Name, Item_Price, Item_CCY, DTInsert) VALUES(?,?) '''
    # cursor.execute(insert_records, name, price)
    # conn.commit()
    #
    #





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



