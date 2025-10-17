from flask import Flask, jsonify, request
from flask_cors import CORS

app1 = Flask(__name__)
CORS(app1)

# -----------------------------
# In-memory data (mock database)
# -----------------------------
accounts = [
    {"AccountID": "A001", "CustomerID": "C001", "AccountType": "Saving", "Balance": 5000.00},
    {"AccountID": "A002", "CustomerID": "C001", "AccountType": "Current", "Balance": 12000.00},
    # {"AccountID": "A003", "CustomerID": "C002", "AccountType": "Savings", "Balance": 15000.00},
]

# -----------------------------
# Routes
# -----------------------------

@app1.route('/')
def home():
    return jsonify({"message": "Bank Account API is running!"})


# ✅ Get all accounts
@app1.route('/api/accounts', methods=['GET'])
def get_accounts():
    return jsonify(accounts)


# ✅ Get a specific account by AccountID
@app1.route('/api/accounts/<account_id>', methods=['GET'])
def get_account(account_id):
    account = next((acc for acc in accounts if acc["AccountID"] == account_id), None)
    if account:
        return jsonify(account)
    return jsonify({"error": "Account not found"}), 404


# ✅ Add a new account
@app1.route('/api/accounts', methods=['POST'])
def add_account():
    new_account = request.get_json()
    accounts.append(new_account)
    return jsonify({"message": "Account added successfully!", "account": new_account}), 201


# ✅ Update an account
@app1.route('/api/accounts/<account_id>', methods=['PUT'])
def update_account(account_id):
    account = next((acc for acc in accounts if acc["AccountID"] == account_id), None)
    if not account:
        return jsonify({"error": "Account not found"}), 404

    updated_data = request.get_json()
    account.update(updated_data)
    return jsonify({"message": "Account updated successfully!", "account": account})


# ✅ Delete an account
@app1.route('/api/accounts/<account_id>', methods=['DELETE'])
def delete_account(account_id):
    global accounts
    accounts = [acc for acc in accounts if acc["AccountID"] != account_id]
    return jsonify({"message": "Account deleted successfully!"})


# -------------------------
# Run the app
# -------------------------
if __name__ == '__main__':
    app1.run(debug=True)