import mysql.connector as mysqlDb

mydb = mysqlDb.connect(
    host= "localhost",
    user = "root",
    password = "",
    database = "mydbonetoone"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM students")
data = mycursor.fetchall()

print(data)