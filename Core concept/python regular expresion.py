import re
text = """
Name: Gaurav Dabade
Email: gaurav123@example.com
Phone: +91-9876543210
Website: https://example.org
Price: $199.99
Date: 18-12-2025
Id Codes: A12 B233 C98Z D-22
Repeated latters hellooooooo!!!
"""


print("\n=== Basic regex methods ===")

# findall
print("findall:", re.findall(r"\d+",text))

# search
match = re.search(r"Gaurav", text)
print("search:",match.group() if match else None)

# match (only checks start)
print("match:", re.match(r"\s*Name",text))

# split
print("split:", re.split(r"\s+", "Python is awesome"))

# sub replace
print("sub replace:", re.sub(r"\d", "*", "P4ssw0rd"))


print("\n=== Character classes ===")
print(re.findall(r"[aeiou]", text))



print(re.findall(r"[A-Z]", text))   # capitals


print(re.findall(r"\w+",text))     # words


print(re.findall(r"\d+", text))    # digits

print(re.findall(r"\s+", text))     # whitespace


print("\n=== Predefined meta characters ===")
print(re.findall(r".", "ABCD"))           # any char
print(re.findall(r"\d", "123abc"))        # digits
print(re.findall(r"\D", "123abc"))        # non-digits
print(re.findall(r"\w", "_a!b"))          # alphanumeric
print(re.findall(r"\W", "_a!b"))          # non-alphanumeric
print(re.findall(r"\s", "Hi there"))      # space
print(re.findall(r"\S", "Hi there"))      # non-space


print("\n=== Groups and capturing ===")
print(re.findall(r"(\w+)@(\w+)\.(\w+)", text))      # email broken into groups


# Email
email = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", text)
print("Email:", email)


# Phone with +91
phone = re.findall(r"\+91[- ]?\d{10}", text)
print("Phone:", phone)


# URL
url = re.findall(r"https?://[^\s]+", text)
print("URL:", url)


# Money
print(re.findall(r"\$\d+(\.\d+)?", text))


# Date dd-mm-yyyy
print(re.findall(r"\d{2}-\d{2}-\d{4}", text))