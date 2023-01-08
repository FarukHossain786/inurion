from database import cursor, mydb
import os, sys

# print(cursor.execute('show tables'))

f = open(os.path.join(sys.path[0], 'glass.data'), "r")
lines = f.readlines()
indexs_data = lines[0].rstrip('\n')
array_index = indexs_data.split(',')

# Check table exist or not
cursor.execute("SHOW TABLES LIKE 'glassdata';")
tables = cursor.fetchall()
if(not tables):
    query = "CREATE TABLE glassdata("
    count = 0
    while count < len(array_index):
        query += "`{}` varchar(50), ".format(array_index[count])
        count += 1 
        
    query = query.rstrip(' ,')
    query +=");" 

    try:
        cursor.execute(query)
    except Exception as ex:
        print(ex)



for i in lines[1: ]:
    datas = i.split(',')
    insert = """INSERT INTO `glassdata`(`"""+"`, `".join(array_index)+"`) values("
    count = 0
    while count < len(datas):
        insert += "'{}', ".format(datas[count])
        count += 1 
        
    insert = insert.rstrip(' ,')
    insert +=");" 

    cursor.execute(insert)
    mydb.commit()

