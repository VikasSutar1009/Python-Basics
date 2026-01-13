def validate(password):
    if len(password) < 8:
        return "Weak Password"
    elif not any (char.isdigit() for char in password):
        return "Add numbers"