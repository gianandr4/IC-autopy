import magic_item_DB_lib as f
# import pandas

# CONNECTION FUNCTION FROM LIB
cursor = f.connect()

# READER FUNCTION FROM lib
l=f.reader(cursor=cursor,to_pandas=False)

# ΤΗΕ ΤΑΒΛΕ
print(l)

# l[0].append('asda')
#
# for item in l[0]:
#     print(type(item),'\n',item)
#     input()
#



