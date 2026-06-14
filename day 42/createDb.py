import mysql.connector as mysqlDb

mydb = mysqlDb.connect(
    host= "localhost",
    user = "root",
    password = ""
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE IF NOT EXISTS mydbonetoone")

print("Database created successfully!")