import mysql.connector

# Connect to MySQL
mydb= mysql.connector(
host="localhost",                     # or your server host
user= "root",                         # your MySQL username
passward="vikas@1020",                # your MySQL passward
database="companies"    # optional: the DB to use
)
print("Connection Success")


# Create a cursor object
mycursor=mydb.cursor()

# create a new table
mycursor.execute(""" 
                 CREATE TABLE IF EXISTS students(
                 id int,
                 name VARCHAR(255),
                 age int
             )
"""    )
print("table created successfully")


# insert data
sql="insert into students (name,age) values(%s,%s)"
val=("vikas",22) 
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount,"record inserted")

