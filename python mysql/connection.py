import mysql.connector

# Replace with your actual database credentials
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="vikas@1020",
  database="employeesconnection"
)

print("Connection Success")
