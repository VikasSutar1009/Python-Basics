import mysql.connector

conn = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'vikas@1020',
    database = 'Python_stored_procedure'
)

cursor = conn.cursor()
print ("Database connected")

# Example 1 - Call a stored Procedure (No Parameters)

cursor.callproc('ShowAllEmoloyee')

# fetch results from the stored procedure
for result in cursor.stored_results():
    rows = result.fetchall()
    for row in rows:
        print(row)


# Example 2 - call procedure with Input parameters

dept = 'IT'
cursor.callproc('GetEmployeeByDept',  [dept])

for result in cursor.stored_results():
    rows = result.fetchall()
    for row in rows:
        print(row)

# Example 3 - Procedure with Output parameter

args = [3,0]  # empid = 3, output param placeholder
result_args = cursor.callproc('GetEmployeeSalary', args)

print('Employee Salary:', result_args[1])

# Example 4 - Insert Data using a procedure

new_emp = (11, 'Meena Reddy', 'Sales', 62000.00)
cursor.callproc('AddEmployee', new_emp)
conn.commit()
print("Employee inserted successfully!")

# Clean Up

# Always close the connection:

cursor.close()
conn.close()
print('Cleaned successfully')