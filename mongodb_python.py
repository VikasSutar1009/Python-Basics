from pymongo import MongoClient

#1. MongoDB connection 
client = MongoClient("mongodb://localhost:27017/")

# Create / select database 
db = client["mydatabase"]

# print("MongoDB connected Successfully!")

from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
collection = db["employee"]

user = {
    "name": "Vikas",
    "email": "vikas@gmail.com",
    "age": 22
}

result = collection.insert_one(user)
print("Inserted ID:", result.inserted_id)

user = collection.find_one({"name": "Vikas"})
print(user)

# Find all 
for user in collection.find():
    print(user)

# Update data
collection.update_one(
    {"name": "Vikas"},
    {"$set": {"age": 26}}
)
print("User Updated")

# Delete data
# collection.delete_one({"name": "Vikas"})

# print("User deleted")