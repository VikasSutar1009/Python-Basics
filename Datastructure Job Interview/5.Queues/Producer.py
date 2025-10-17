for i in range(5):
    if len(buffer) < buffer.maxlen:
        buffer.append(i)
        print("Produced:", i)