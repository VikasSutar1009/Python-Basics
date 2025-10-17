from flask import Flask, jsonify, request
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)

# ---------------------------
# MySQL Database Configuration
# ---------------------------
db_config = {
    'host': 'localhost',
    'user': 'root',          # change if needed
    'password': '',          # your MySQL password
    'database': 'flask_api_demo'
}

# Function to get a DB connection
def get_db_connection():
    return mysql.connector.connect(**db_config)

# ---------------------------
# Root Route
# ---------------------------
@app.route('/')
def home():
    return jsonify({"message": "Welcome to Flask MySQL REST API!"})

# ---------------------------
# GET all users
# ---------------------------
@app.route('/api/users', methods=['GET'])
def get_users():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(rows)

# ---------------------------
# GET one user by ID
# ---------------------------
@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
    row = cursor.fetchone()
    cursor.close()
    conn.close()
    if row:
        return jsonify(row)
    return jsonify({"error": "User not found"}), 404

# ---------------------------
# POST - Add new user
# ---------------------------
@app.route('/api/users', methods=['POST'])
def add_user():
    data = request.get_json()
    if not data or 'name' not in data or 'email' not in data:
        return jsonify({"error": "Invalid input"}), 400

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO users (name, email) VALUES (%s, %s)",
        (data['name'], data['email'])
    )
    conn.commit()
    new_id = cursor.lastrowid
    cursor.close()
    conn.close()
    return jsonify({"id": new_id, "name": data['name'], "email": data['email']}), 201

# ---------------------------
# PUT - Update user
# ---------------------------
@app.route('/api/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE users SET name = %s, email = %s WHERE id = %s",
        (data.get('name'), data.get('email'), user_id)
    )
    conn.commit()
    affected = cursor.rowcount
    cursor.close()
    conn.close()

    if affected == 0:
        return jsonify({"error": "User not found"}), 404

    return jsonify({"message": "User updated successfully"})

# ---------------------------
# DELETE - Delete user
# ---------------------------
@app.route('/api/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
    conn.commit()
    affected = cursor.rowcount
    cursor.close()
    conn.close()

    if affected == 0:
        return jsonify({"error": "User not found"}), 404

    return jsonify({"message": "User deleted successfully"})

# ---------------------------
# Run App
# ---------------------------
if __name__ == '__main__':
    app.run(debug=True)