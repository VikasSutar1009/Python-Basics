from flask import Flask, jsonify, request
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)

# .................................
# Mysql databas configuration
#....................................
db_config = {
    'host': 'localhost:3306',
    'user': 'root',                 # Change if needed
    'password': 'vikas@1020',       # Your MySQL password
    'database': 'flask_api_demo'
}

# function to get a DB connection
def get_db_connection():
    return mysql.connector.connect(**db_config)

# ....................................
# Root route
# ......................................
@app.route('/')
def home():
    return jsonify({'message': 'welcome to Flask MySQL REST API !'})

# ....................................
# GET all users
# ....................................
@app.route('/api/users', methods = ['GET'])
def get_users():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('select * from users')
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(rows)

# ....................................
# GET one user by ID
# ....................................
@app.route('/api/users/<int:user_id>', methods = ['GET'])
def get_user(user_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('select * from users where  id = %s', (user_id))
    row =  cursor.fetchone()
    cursor.close()
    conn.close()
    if row :
        return jsonify(row)
    return jsonify({'error': 'user not found'}), 404

# ...................................
# POST = Add new user
# ...................................
@app.route('/api/users', methods = ['POST'])
def add_user():
    data = request.get_json()
    if not data or 'name' not in data or 'email' not in data:
        return jsonify({'error': 'Invalid input'}), 400
    
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        'insert into users (name, email) values (%s, %s)',
        (data['name'], data['email'])
    )
    conn.commit()
    new_id = cursor.lastrowid
    cursor.close()
    conn.close()
    return jsonify({'id': new_id, 'name': data['name'], 'email': data['email']}), 201

# ....................................
# PUT = Update  user
# ....................................
@app.route('/api/users/<int:user_id>', methods = ['PUT'])
def update_user(user_id):
    data = request.get_json()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        'update users set name = %s, email = %s where id = %s',
        (data.get('name'), data.get('email'), user_id)
    )
    conn.commit()
    affected = cursor.rowcount
    cursor.close()
    cursor.close()

    if affected == 0:
        return jsonify({'error': 'user not found'}), 404
    
    return jsonify({'message': 'user updated successfully'})

# ...................................
# DELET = Delete user
# ....................................
@app.route('/api/users/<int:user_id>', methods = ['DELETE'])
def delete_user(user_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('delete from users where id = %s', (user_id))
    conn.commit()
    affected = cursor.rowcount
    cursor.close()
    conn.close()

    if affected == 0:
        return jsonify({'error': 'user not found'}), 404
    
    return jsonify({'message': 'user deleted successfully'})

# .................................
# Run App
# .................................
if __name__ == "__main__":
    app.run(debug=True)

