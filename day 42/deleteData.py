import mysql.connector as mysqlDb

mydb = mysqlDb.connect(
    host= "localhost",
    user = "root",
    password = "",
    database = "mydbonetoone"
)

mycursor = mydb.cursor()

mycursor.execute("DELETE FROM students WHERE name = 'Pragyann'")
mydb.commit()
print("Data deleted successfully!")