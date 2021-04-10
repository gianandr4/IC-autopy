import magic_item_DB_lib as f
import datetime
conn=f.connect()#################################### CONNECTION FUNCTION FROM LIB





#################################################### READER FUNCTION FROM lib
table=f.reader(conn=conn,to_pandas=False)
print('\nLast Insert:')
print(table[-1][-1],table[-1][0],'---->',table[-1][-4],'\n')
if input('Print table? (yes)').lower()=='yes':
    for i in table:
        print(i)


#################################################### WRITER FUNCTION (COMMIT)

if input('Do you wish to insert? (yes)').lower()=='yes':

    itemz=[]
    for i in range(10):
        itemz.append({'Item_Name':input('Item_Name'), 'Item_Price': i*100, 'Item_CCY': 'gp','Note':'Test', 'DTInsert': datetime.datetime.now()})



    # dict = {'Item_Name':'Severed Hand', 'Item_Price': 100, 'Item_CCY': 'gp','Note':'Test', 'DTInsert': datetime.datetime.now()}
    for dict in itemz:
        f.writer(conn=conn,item_dict=dict)
    conn.commit()


#################################################### DELETER FUNCTION (COMMIT)
if input('Do you wish to delete? (yes)').lower()=='yes':
    print('______________________________________________________________')
    delstr='''WHERE Item_ID>70 AND Note='Test' '''
    f.deleter(conn,filter=delstr)

#################################################### CLOSE CONNECTION
conn.close()
