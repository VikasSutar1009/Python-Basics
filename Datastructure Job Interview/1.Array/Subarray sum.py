nums = [1, -3, 2, 1, -1]
max_sum = curr = nums[0]
for n in nums[1:]:
    curr = max(n, curr+n)
    max_sum = max(max_sum, curr)
print("Max Subarray Sum:", max_sum)