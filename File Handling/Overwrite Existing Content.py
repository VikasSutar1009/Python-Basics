# open the file "demo.txt",and overwrite the content:

with open("demo.txt","w") as f:
    f.write("Woops! I have deleted the content!")

with open("demo.txt")as f:
    print(f.read())