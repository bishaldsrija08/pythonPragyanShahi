import mysql.connector as mysqlDb

mydb = mysqlDb.connect(
    host= "localhost",
    user = "root",
    password = "",
    database = "mydbonetoone"
)

mycursor = mydb.cursor()

mycursor.execute("INSERT INTO students (id, name, age) VALUES (1, 'Alice', 20)")

mydb.commit()

print("Data inserted successfully!")