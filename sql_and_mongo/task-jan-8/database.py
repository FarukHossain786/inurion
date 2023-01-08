import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="useradmin"
)
cursor = mydb.cursor()
cursor.execute("use glassdata")