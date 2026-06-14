import mysql.connector as mysqlDb

mydb = mysqlDb.connect(
    host= "localhost",
    user = "root",
    password = "",
    database = "mydbonetoone"
)

mycursor = mydb.cursor()

mycursor.execute("UPDATE students SET age = 12 WHERE name = 'Pragyan'")
mydb.commit()   
print("Data updated successfully!")