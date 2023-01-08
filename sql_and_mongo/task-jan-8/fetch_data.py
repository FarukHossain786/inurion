from database import cursor

cursor.execute('SELECT * FROM glassdata')
for i in cursor.fetchall():
    print(i)
