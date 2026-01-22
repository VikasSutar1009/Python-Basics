# 1
def details(**data):
    print(data)

# 2
def student(**info):
    print(info["name"], info["age"])

# 3
def profile(**kwargs):
    for k, v in kwargs.items():
        print(k, "=", v)

# 4
def employee(**emp):
    print(emp.get("salary"))

# 5
def login(**user):
    if user["username"] == "admin":
        print("Welcome")

# 6
def billing(**items):
    print(sum(items.values()))

# 7
def address(**addr):
    print(addr)

# 8
def car(**details):
    print(details["brand"], details["model"])

# 9
def marks(**subject):
    print(subject)

# 10
def config(**settings):
    print(settings)
    