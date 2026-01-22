from db.db_config import get_connection
from services .auth_service import generate_token

def register_user(**user):
    conn = get_connection()
    cursor = conn.cursor()

    query = "INSERT INTO users(name, email, password) VALUES(%s,%s,%s)"
    cursor.execute(query, (user["name"], user["email"], user["password"]))

    conn.commit()
    print("User Registered Successfully")

def login_user(email, password):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE email = %s AND password = %s",
        (email, password)
    )

    user = cursor.fetchone()

    if user:
        token = generate_token(user[0])
        return token
    return None
