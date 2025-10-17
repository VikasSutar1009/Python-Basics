# Q10. Nested List Processing (12.5 Marks)
# Given the nested list matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]. Write a Python code block to calculate the sum of all elements in the entire nested list. Store the final sum in a variable called total_sum.
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
total_sum = 0
for row in matrix:
    total_sum += sum(row)
print(total_sum)