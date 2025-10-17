s = "abcabcbb"
seen, start, longest = {}, 0, 0
for i, ch in enumerate(s):
    if ch in seen and seen[ch] >= start:
        start = seen[ch] + 1
    seen[ch] = i
    longest = max(longest, i - start + 1)
print("Longest unique substring length:", longest)