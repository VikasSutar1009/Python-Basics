# Creating a list
numbers = [10, 20, 30, 40]


# Accessing list
print(numbers[0])
print(numbers[-1])


# Slicing a list
nums = [10,20,30,40,50]

print(nums[1:4])
print(nums[:3])
print(nums[::2])

# Changing list elements
nums = [10,20,30]
nums[1] = 99
print(nums)

# Adding elements to list
# append
nums = [1,2,3]
nums.append(4)

# print(nums)

# insert
nums.insert(1,100)
print(nums)

# extend
nums.extend([5,6])
print(nums)

# Remove elements
nums.remove(100)
print(nums)

# pop
nums.pop()
print(nums)

# clear
nums.clear()
print(nums)

# List Length
nums=[10,20,30]
print(len(nums))

# Sorting a List
nums = [40,10,30,20]

nums.sort()
print(nums)      # [10,20,30,40]

nums.sort(reverse=True)
print(nums)      # [40,30,20,10]


# Reverse a List
nums = [1,2,3]
nums.reverse()

print(nums)


# Finding Elements
# index
nums=[10,20,30]
print(nums.index(20))


# count
nums = [10,20,20,30]
print(nums.count(20))

# Membership(in / not in)
nums = [10,20,30]

print(20 in nums)
print(40 not in nums)


# Looping Through List
nums = [10,20,30]
for n in nums:
    print(n)


# List comprehension(very important)
squares = [x*x for x in range(1,6)]
print(squares)


# Copying a List
nums = [1,2,3]

copy1 = nums.copy()
copy2 = nums[:]

# Joining List
a=[1,2]
b=[3,4]

c= a+b
print(c)


# Nested List
matrix = [[1,2],[3,4],[5,6]]

print(matrix[1][0])