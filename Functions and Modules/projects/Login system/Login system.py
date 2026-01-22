users = {"admin": "1234"}

def login(**data):
    if data["username"] in users and users[data["username"]] == data["password"]:
        print("Login Successful")
    else:
        print("Invalid Credentials")

login(username = "admin", password = "1234")
