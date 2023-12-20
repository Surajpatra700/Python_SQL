import mysql.connector

mydb = mysql.connector.connect(user='root', password='Suraj@2003',
    host='127.0.0.1', 
    database= "testdb"
)

# Cursor is an object that communicates with mysql server
mycursor = mydb.cursor()

# ************ CREATING DATABASE *********************

mycursor.execute("CREATE DATABASE testdb")

# ******************* CREATING TABLE IN DATABASE **************

mycursor.execute("CREATE TABLE students (name VARCHAR(255), age INTEGER(5))")

#  *********************** Displaying tables in our Workbench *****************

mycursor.execute("SHOW TABLES")

for tb in mycursor:
    print(tb)

# *********************** INSERTING DATA TO DATABASE ********************

sqlformula = "INSERT INTO students (name, age) VALUES(%s, %s)"

# FOR SINGLE TUPLE ENTRY INTO DATABASE

student1 = ("Suraj Patra",20)
mycursor.execute(sqlformula,student1)

# FOR MULTILPLE TUPLE ENTRY INTO DATABASE

students = [
    ("Suraj Patra",20),
    ("Jaghanya Rajput",40),
    ("Pulkit Samrat", 28)
]

mycursor.executemany(sqlformula,students)

# mydb.commit() ---> to commit changes to database
mydb.commit()

# ********************* RETRIEVING DATA FROM DATABASE ****************

mycursor.execute("SELECT * FROM students")
mycursor.execute("SELECT name FROM students WHERE age = 28")
mycursor.execute("SELECT age FROM students WHERE name LIKE 'Su%'")

#  ********* 'Su%' means that the "Su" character is present at the start of name 
#  ********* '%Su%' means that the "Su" character is present at the somewhat middle of name 
#  ********* '%Su' means that the "Su" character is present at the last of name 

results = mycursor.fetchall()
print(results)

# for data in results:
#     print(data)

# ********************* UPDATING DATA FROM DATABASE ****************

sql = "UPDATE students SET age= 55 WHERE name='Suraj Patra'"
mycursor.execute(sql)
mydb.commit()

# ************** Limiting Count of Return Values ***********

mycursor.execute("SELECT * FROM students LIMIT 2 OFFSET 2")
myResult = mycursor.fetchall()

for results in myResult:
    print(results)

# ********************** ORDERING OUR QUERIES AND RESULTS ********************

# ascending order ordering of name
sql = "SELECT * FROM students ORDER BY name"

# descending order ordering of name
sql = "SELECT * FROM students ORDER BY name DESC"
mycursor.execute(sql)
myresults = mycursor.fetchall()
for results in myresults:
    print(results)

# ************************* DELETING DATA FROM DATABASE ******************

sql = "DELETE FROM students WHERE name='Suraj Patra'"
mycursor.execute(sql)
mydb.commit()

# ************************ DELETING ENTIRE TABLE ***************************

sql = "DELETE TABLE students"
mycursor.execute(sql)
mydb.commit()