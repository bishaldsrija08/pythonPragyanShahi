import mysql.connector as mysqlDb

mydb = mysqlDb.connect(
    host= "localhost",
    user = "root",
    password = ""
)

print(mydb, "Connected to MySQL database successfully!")