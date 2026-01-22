# 1
def add(*nums):
    return sum(nums)

# 2
def show(*args):
    print(args)

# 3
def average(*nums):
    return sum(nums) / len(nums)

# 4
def names(*students):
    for s in students:
        print(s)

# 5
def multiply(*nums):
    result = 1
    for n in nums:
        result *= n
    return result

# 6
def check(*values):
    print(type(values))   # tuple

# 7
def max_value(*nums):
    return max(nums)

# 8
def min_value(*nums):
    return min(nums)

# 9
def even_numbers(*nums):
    return [n for n in nums if n % 2 == 0]

# 10
def show_len(*items):
    print(len(items))