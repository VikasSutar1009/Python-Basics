# Open the file "demofile.txt" and append content to the file:

with open("demo.txt","a") as f:
    f.write(" Now the file has more content!")

#open and read the file after the appending:
with open("demo.txt") as f:
    print(f.read())