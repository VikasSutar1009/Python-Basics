''' import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="vikas@1020",
    database="python_mysql_connection"
)

print("Connection Success") '''

import mysql.connector
from mysql.connector import Error

try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="vikas@1020",
        database="python_mysql_connection"
    )

    if mydb.is_connected():
        print("Connection Success")

except Error as e:
    print("Error while connecting to MySQL:", e)
