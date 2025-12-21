# === ALL OPERATIONS IN ONE PYTHON SCRIPT ===

# ------------------------------
# 1. Arithmetic
# ------------------------------
a, b = 10, 3

print("Arithmetic operations:")
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)

# ------------------------------
# 2. Comparison operators
# ------------------------------
print("\nComparison operations:")
print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)

# ------------------------------
# 3. Logical operators
# ------------------------------
x, y = True, False

print("\nLogical operations:")
print(x and y)
print(x or y)
print(not x)

# ------------------------------
# 4. Bitwise operators
# ------------------------------
print("\nBitwise operations:")
print(a & b)
print(a | b)
print(a ^ b)
print(~a)
print(a << 1)
print(a >> 1)

# ------------------------------
# 5. Assignment operators
# ------------------------------
print("\nAssignment operations:")
c = 5
c += 2
print(c)
c -= 1
print(c)
c *= 3
print(c)
c //= 2
print(c)

# ------------------------------
# 6. List operations
# ------------------------------
print("\nList operations:")
lst = [1, 2, 3]
lst.append(4)
lst.insert(0, 0)
lst.extend([5,6])
print(lst)
lst.pop()
print(lst)
lst.reverse()
print(lst)

# ------------------------------
# 7. String operations
# ------------------------------
print("\nString operations:")
s = "hello world"
print(s[0:5])
print(s.upper())
print(s.replace("world","python"))
print(" ".join(["welcome","to","python"]))
print(s.split())

# ------------------------------
# 8. Set operations
# ------------------------------
print("\nSet operations:")
s1 = {1,2,3}
s2 = {3,4,5}
print(s1 | s2)  # union
print(s1 & s2)  # intersection
print(s1 - s2)  # difference
print(s1 ^ s2)  # symmetric diff

# ------------------------------
# 9. Dictionary operations
# ------------------------------
print("\nDictionary operations:")
d = {"name":"Gaurav","age":25}
d["role"] = "engineer"
print(d.keys())
print(d.values())
print(d.items())
del d["age"]
print(d)

# ------------------------------
# 10. File operations
# ------------------------------
print("\nFile operations:")

with open("test.txt","w") as f:
    f.write("Hello Python")

with open("test.txt","r") as f:
    print(f.read())