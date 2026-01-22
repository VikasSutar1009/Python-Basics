def quiz():
    score = 0
    if input("Python is case sensitive? (yes/no): ") == "yes":
        score += 1
    if input("Is Python interpreted? (yes/no): ") == "yes":
        score += 1
    print("Score:", score)
quiz()