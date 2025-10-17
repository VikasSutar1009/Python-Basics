# Q13. Merge two dictionaries into one.
bikes={
    "brand":"hero",
    "model":"splender",
    "color":"black"
}

name={
    "name":"vikas",
    "city":"ajara",
    "age":22
}
z={**bikes , **name}
print(z)

