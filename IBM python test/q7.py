# Q7. Deep vs. Shallow Copy (5 Marks)
#Given the list original = [1, [2, 3], 4]. Create a true, independent copy of original named independent_copy. Then, change the first element of independent_copy to 100. Print both lists to demonstrate the independence. (Hint: A simple assignment or list() constructor won't suffice for the nested element).
import copy

original = [1, [2, 3], 4]
# Use copy.deepcopy() for a fully independent copy
independent_copy = copy.deepcopy(original) 

independent_copy[0] = 100

print(f"Original List: {original}")
print(f"Independent Copy: {independent_copy}")

# Expected Output:
# Original List: [1, [2, 3], 4]
# Independent Copy: [100, [2, 3], 4]