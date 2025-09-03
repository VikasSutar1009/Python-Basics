#import mysql.connector

'''mydb =mysql.connector.connect(
    host="localhost",
    user="root",
    password="vikas@1020",
    database="employees"
)
print("connection successful")'''

import mysql.connector
from mysql.connector import Error

try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="vikas@1020",
        database="employees"
    )

    if mydb.is_connected():
        print("Connection successful")
    else:
        print("Connection failed")

except Error as e:
    print("Error while connecting to MySQL:", e)


#mycursor= mydb.curosr()

#mycursor.execute("""
 #                create table if not exists employee(
  #               empid int auto_increment primary key,
   #              name varchar(100),
    #             department varchar(50),
     #            salary decimal(10,2)
      #           joindate date
       #          )
#""")
#print("employee table created successfully.")

# sql = "INSERT INTO employee(name, department, salary, joindate) values(%s,%s,%s,%s)"
# values=[
    # ("Alice","HR",50000.00, date(2020,1,15)),
 #   ("Bob","IT",75000.00, date(2019,5,10)),
  #  ("Charlie","Finance",62000.00, date(2021,7,22)),
   # ("David","IT",80000.00,date(2018,3,28)),
    #("Eva","HR",48000.00,date(2022,2,28))
#]

#mycursor.executemany(sql, values)
#mydb.commit()

#print(mycursor.rowcount,"records inserted.")

#mycursor = mydb.cursor()

#sql="update employee set salary=salary + 5000 where department ='HR' "
#mycursor.execute(sql)
#mydb.commit()

#print(mycursor.rowcount,"record(s) updated.")

#mycursor = mydb.cursor()

#mycursor.execute("select avg(salary) from employee")
#print("average salary:", mycursor.fetchone()[0])

#mycursor.execute("select sum(salary) from employee")
#print("total salary:",mycursor.fetchone()[0])

#mycursor.execute("select min(salary) from employee")
#print("minimum salary:",mycursor.fetchone()[0])

#mycursor.execute("select max(salary) from employee")
#print("maximum salary:",mycursor.fetchone()[0])

#mycursor.execute("select count(*) from employee")
#print("total employees:",mycursor.fetchone()[0])

