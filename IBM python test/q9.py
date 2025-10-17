# Q9. Conditional List Comprehension (12.5 Marks)
# Using a single line of code with a list comprehension, create a new list named evens_squared from the list numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]. The new list should only contain the square of the elements from the original list that are even numbers.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens_squared = [x**2 for x in numbers if x % 2 ==0]
print(evens_squared)