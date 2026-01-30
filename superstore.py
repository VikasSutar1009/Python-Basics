from pymongo import MongoClient

# 1. MongoDB connection
client = MongoClient("mongodb://localhost:27017/")

# Create / select database
db = client["supermarket"]

# print("MongoDB connected successfully")

# Create collections
customer_collection = db["customer"]
product_collection = db["product"]
orders_collection = db["orders"]


# INSERT CUSTOMER
customer = {
    "customer_id": "c001",
    "name": "Vikas",
    "email": "vikas@gmail.com",
    "phone": "9158257510"
}

# customer_collection.insert_one(customer)
# print("Customer inserted successfully")

# INSERT PRODUCT
product = {
    "product_id": "p001",
    "name": "HP Laptop",
    "category": "Electronics",
    "price": 70000
}

# product_collection.insert_one(product)
# print("Product inserted successfully")


# INSERT ORDER

order = {
    "order_id": "o1001",
    "customer_id": "c001",
    "product_id": "p001",
    "quantity": 2,
    "total_amount": 140000
}

# orders_collection.insert_one(order)
# print("Order inserted successfully")


# FIND DATA

# print("\nCustomers:")
# for c in customer_collection.find():
#     print(c)

# print("\nProducts:")
# for p in product_collection.find():
#     print(p)

# print("\nOrders:")
# for o in orders_collection.find():
#     print(o)


# UPDATE DATA

# customer_collection.update_one(
#     {"customer_id": "c001"},
#     {"$set": {"email": "vikas1020@gmail.com"}}
# )
# print("Customer updated")

# product_collection.update_one(
#     {"product_id": "p001"},
#     {"$set": {"price": 70000}}
# )
# print("Product updated")


# DELETE DATA

# orders_collection.delete_one({"order_id": "o1001"})
# print("Order deleted")


# CLOSE CONNECTION

client.close()
print("MongoDB connection closed")