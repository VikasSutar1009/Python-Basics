from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

users = [
    {'id': 101,'product_name': 'Milk 1L', 'price': 45},
    {'id': 102,'product_name': 'Bread', 'price': 30}
]

# Get message

@app.route('/')
def home():
    return jsonify({'message': 'Welcome to the REST api!'})

# Get all values

@app.route('/api/users', methods = ['GET'])
def get_users():
    return jsonify(users)

# POST
@app.route('/api/users/<int:user_id>', methods = ['POST'])
def add_users():
    data = request.get_json()
    if not data or 'product_name' not in data or 'price' not in data:
        return jsonify({'error': 'invalid data'}), 400
    new_id = max([u['id'] for u in users]) + 1 if users else 1
    new_user = {'id': new_id, 'product_name': data['product_name'], 'price':data['price']}
    users.append(new_user)
    return jsonify(new_user), 201

# PUT
@app.route('/api/users<int:user_id>', methods = ['PUT'])
def update_users():
    data = request.get_json()
    user = next((u for u in users if u['id'] == id), None)

    if not user:
        return jsonify({'error': 'user not found!'}), 404
    
    user['product_name'] = data.get ('product_name', user['product_name'])
    user['price'] = data.get ('price', user['price'])
    return jsonify(user)



# DELETE
@app.route('/api/users<int:user_id>', methods = ['DELETE'])
def delete_user(user_id):
    global users
    users = [u for u in users if u ['id'] != user_id]
    return jsonify({'message':'data deleted successfully!'})

if __name__ == '__main__':
    app.run(debug=True)