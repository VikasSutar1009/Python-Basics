def write_log(message):
    with open("app.log", "a") as f:
        f.write(message + "\n")

write_log("User logged in")
write_log("Transaction successful")