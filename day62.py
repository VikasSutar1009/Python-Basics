import mysql.connector

# Connect to MySQL
mydb= mysql.connector(
    host="localhost",                     # or your server host
    user= "root",                         # your MySQL username
    passward="vikas@1020",                # your MySQL passward
    database="companies"                  # optional: the DB to use
    )
print("Connection Success")

