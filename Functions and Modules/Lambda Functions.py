# 1
square = lambda x: x*x

# 2
add = lambda a,b: a + b

# 3
even = lambda x: x % 2 == 0

# 4
max_val = lambda a,b: a if a > b else b

# 5
length = lambda s: len(s)

# 6
upper = lambda s: s.upper()

# 7
square_list = list(map(lambda x: x * x, [1,2,3]))

# 8
even_list = list(filter(lambda x: x%2==0, [1,2,3,4]))

# 9
sort_by_length = sorted(["cat", "elephant", "dog"], key=lambda x:len(x))

# 10
sum_all = lambda *args: sum(args)