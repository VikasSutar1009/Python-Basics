import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to SQLite (in-memory for demo)
conn = sqlite3.connect(":memory:")
cur = conn.cursor()

# Create tables
cur.execute("CREATE TABLE Departments(DeptID INT, DeptName TEXT)")
cur.execute("CREATE TABLE Employees(EmpID INT, Name TEXT, Salary REAL, DeptID INT)")

# Insert data
cur.executemany("INSERT INTO Departments VALUES (?,?)", [(1,"HR"),(2,"IT"),(3,"Finance")])
cur.executemany("INSERT INTO Employees VALUES (?,?,?,?)", [
    (1,"Alice",50000,1),
    (2,"Bob",60000,2),
    (3,"Charlie",55000,2),
    (4,"David",70000,3),
    (5,"Eva",65000,1),
    (6,"Frank",72000,3)
])
conn.commit()

# Average salary per department
df_avg = pd.read_sql("""
SELECT d.DeptName, AVG(e.Salary) AS AvgSalary
FROM Employees e JOIN Departments d ON e.DeptID=d.DeptID
GROUP BY d.DeptName
""", conn)

# Employees earning above company average
df_above = pd.read_sql("""
SELECT Name, Salary FROM Employees
WHERE Salary > (SELECT AVG(Salary) FROM Employees)
""", conn)

# Plot average salary per department
df_avg.plot(x="DeptName", y="AvgSalary", kind="bar", legend=False)
plt.title("Average Salary per Department")
plt.ylabel("Avg Salary")
plt.show()

print("Employees earning above company average:\n", df_above)

conn.close()
