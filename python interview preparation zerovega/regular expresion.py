import re
txt = "The tain in Spain"

x = re.search("^The.*Spain$", txt)

if x:
    print("Yes! we have a match!")
else:
    print("No match")


# The findall() Function
txt = "The rain in Spain."
x = re.findall("ai", txt)
print(x)

# Search for the first white-space character in the string:
import re

txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position: ", x.start())