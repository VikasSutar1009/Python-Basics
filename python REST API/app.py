from flask import Flask, jsonify, request
from flask_cors import CORS

app =  Flask(__name__)
CORS(app) #enable cross-origin requsts

# In-memory data store (no database)
users = [
    {'id': 1, 'name': 'Alice', 'email': 'alice@example.com'},
    {'id': 2, 'name': 'Bob', 'email': 'bob@example.com'}
]

# ..........................
# React Route
# ..........................
@app.route('/')
def home():
    return jsonify({'message': 'Welcome to th user REST API!'})

# ............................
# GET all users
# ............................
@app.route('/api/users', methods = ['GET'])
def get_users():
    return jsonify(users)

# .............................
# GET one user by ID
# ..............................
@app.route('/api/users/<int:user_id>', methods = ['GET'])
def get_user(user_id):
    user = next((u for u in users if u['id'] == user_id), None)
    if user:
        return jsonify(user)
    return jsonify({'error': 'user not found'}), 404

# ...............................
# POST - Add row user
# ..................................
@app.route('/api/users', methods = ['POST'])
def add_user():
    data = request.get_json()
    if not data or 'name' not in data or 'email' not in data:
        return jsonify({'error': 'invalid data'}), 400
    
    new_id = max([u['id'] for u in users]) + 1 if users else 1
    new_user = {'id': new_id, 'name': data['name'], 'email': data['email']}
    users.append(new_user)
    return jsonify(new_user), 201

# .................................
# PUT - Update user
# .................................
@app.route('/api/users/<int:user_id>', methods = ['PUT'])
def update_user(user_id):
    data  = request.get_json()
    user = next((u for u in users if u['id'] == user_id), None)

    if not user:
        return jsonify({'error': 'User not found'}), 404
    
    user['name'] = data.get('name', user['name'])
    user['email'] = data.get('email', user['email'])
    return jsonify(user)

# ......................................
# DELETE = Delete user
# ......................................
@app.route('/api/users/<int:user_id>', methods = ['DELETE'])
def delete_user(user_id):
    global users
    users = [u for u in users if u['id'] != user_id]
    return jsonify({'message': 'user deleted'})

# ......................................
# Run the Flask app
# .......................................
if __name__ == '__main__':
    app.run(debug=True)