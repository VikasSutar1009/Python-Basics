# # Example 1: Print numbers 1 to 5
# for i in range(1, 6):
#     print(i)

# # Example 2: Loop over a list
# cars = ['bugati', 'farari', 'rolls royals']
# for car in cars:
#     print(car)

# # Example 3: Loop over a string
# # string = 'Vikas'
# # for item in string:
# #     print(item)
# for ch in "PYTHON":
#     print(ch)

# # Example 4: range() variations
# for i in range(2,11,2):            # start=2, stop=11, step2
#     print(i)

# Example 5: Using break and continue
# for i in range(1,10):
#     if i == 5:
#         break      # stop loop
#     print(i)

# for i in range(1,10):
#     if i == 5:
#         continue    # skip 5
#     print(i)

# Nested Loops
# Loops inside loops - used in matrices, patterns, etc.
# for i in range(1,4):
#     for j in range(1,4):
#         print(i,j)

# loop with else
for i in range(3):
    print(i)
else:
    print('Loop completed!')

# Loop with enumerate()
names = ['Amit', 'Neha', 'Raj']
for index, name in enumerate(names):
    print(index, name)