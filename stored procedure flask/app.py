from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

# Database connection function
def get_db_connection():
    return mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = 'vikas@1020',
        database = 'stored_procedure_flask'
    )

# @app.route('/')
# def show_employees():
#     try:
#         conn = get_db_connection()
#         cursor = conn.cursor(dictionary=True)

#         # call stored procedure
#         cursor.callproc('ShowAllEmployees')

#         employees = []
#         for result in cursor.stored_results():
#             enployees = result.fetchall()

#         return render_template('employees.html', employees = employees)
    
#     except mysql.connector.Error as err:
#         return f'Database error: {err}'
    
#     finally:
#         if conn.is_connected():
#             cursor.close()
#             conn.close()

@app.route('/')
def show_employees():
    conn = None
    cursor = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.callproc('ShowAllEmployees')

        employees = []
        for result in cursor.stored_results():
            employees = result.fetchall()

        return render_template('employees.html', employees=employees)

    except mysql.connector.Error as err:
        return f"❌ Database error: {err}"

    finally:
        if cursor:
            cursor.close()
        if conn and conn.is_connected():
            conn.close()
    
# Run Flask app
if __name__ == '__main__':
    app.run(debug=True)