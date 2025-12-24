import mysql.connector

conn = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'vikas@1020',
    database = 'test_db'
)

# print(conn.is_connected())

# Create Cursor
cursor = conn.cursor()

# create table
# cursor.execute("""
# create table if not exists students(
#     id int ,
#     name varchar(100),
#     age int,
#     city varchar(50)
# )
# """)

# print("Table created")

# insert data

# insert_query = """
# INSERT INTO students (id, name, age, city)
# VALUES (%s,%s,%s,%s)
# """

# data = (1, "Amit", 22, "Pune")
# cursor.execute(insert_query, data)
# conn.commit()
# print("1 record inserted")

# data = (2, "Priya", 23, "Mumbai")
# cursor.execute(insert_query, data)
# conn.commit()
# print("2 record inserted")

# data = (3, "Sushant", 24, "Benglore")
# cursor.execute(insert_query, data)
# conn.commit()
# print("3 record inserted")

# data = (4, "Pavan", 20, "Delhi")
# cursor.execute(insert_query, data)
# conn.commit()
# print("4 record inserted")

# data = (5, "Pankaj", 22, "Kolhapur")
# cursor.execute(insert_query, data)
# conn.commit()
# print("5 record inserted")


# select data
# cursor.execute("SELECT * FROM students")

# rows = cursor.fetchall()

# for row in rows:
#     print(row)

# SELECT with WHERE
# cursor.execute("SELECT name, city FROM students WHERE age> %s", (22,))
# result = cursor.fetchall()

# for r in result:
#     print(r)

# UPDATE DATA
# update_query = """
# UPDATE students 
# SET city = %s 
# WHERE name = %s
# """

# cursor.execute(update_query,("Hyderabad", "Amit"))
# conn.commit()

# print("Record updated")

# DELETE DATA 
# delet_query = "DELETE FROM students WHERE name = %s"

# cursor.execute(delet_query,("Pavan",))
# conn.commit()

# print("Record deleted")