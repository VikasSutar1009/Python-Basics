import jwt
import datetime

SECRET_KEY = 'MY_SECRET_KEY'

def generate_token(user_id):
    payload = {
        "user_id": user_id,
        "exp": datetime.date.utcnow() + datetime.timedelta(hours =2)

    }

    token = jwt.ecoded(payload, SECRET_KEY, algorithm = "HS256")
    return

def verify_token(token):
    try:
        decoded = jwt(token, SECRET_KEY, algorithms = ["HS256"])
        return decoded["user_id"]
    except jwt.ExpiredSignatureError:
        return "Token Expired"
    except jwt.InvalidTokenError:
        return "Invalid Token"