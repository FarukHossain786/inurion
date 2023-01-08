import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="useradmin"
)
print(mydb)

mycursor = mydb.cursor()
mycursor.execute('create database ineuron')