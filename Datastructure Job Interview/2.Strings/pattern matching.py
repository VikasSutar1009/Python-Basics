text, pat = "ababcabc", "abc"
for i in range(len(text)-len(pat)+1):
    if text[i:i+len(pat)] == pat:
        print("Pattern found at index:", i)