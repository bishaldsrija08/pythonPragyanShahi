import mysql.connector as mysqlDb

mydb = mysqlDb.connect(
    host= "localhost",
    user = "root",
    password = "",
    database = "mydbonetoone"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE IF NOT EXISTS students (id INT, name VARCHAR(255), age INT)")

print("Table created successfully!")