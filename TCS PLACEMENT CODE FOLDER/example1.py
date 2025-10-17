# Problem Statement –
# A chocolate factory is packing chocolates into the packets. The chocolate packets here represent an array  of N number of integer values. The task is to find the empty packets(0) of chocolate and push it to the end of the conveyor belt(array).
# Example 1 :
# N=8 and arr = [4,5,0,1,9,0,5,0].
# There are 3 empty packets in the given set. These 3 empty packets represented as O should be pushed towards the end of the array
# Input :
# 8  – Value of N
# [4,5,0,1,9,0,5,0] – Element of arr[O] to arr[N-1],While input each element is separated by newline
# Output:
# 4 5 1 9 5 0 0 0
# Example 2:
# Input:
# 6 — Value of N.
# [6,0,1,8,0,2] – Element of arr[0] to arr[N-1], While input each element is separated by newline
# Output:
# 6 1 8 2 0 0

# Function to push all zeros to the end of the array
def push_zeros_to_end(arr, N):
    pos = 0  # position to place the next non-zero element

    # Move all non-zero elements to the front
    for i in range(N):
        if arr[i] != 0:
            arr[pos] = arr[i]
            pos += 1

    # Fill remaining positions with zero
    while pos < N:
        arr[pos] = 0
        pos += 1

    return arr

# Input reading
N = int(input("Enter number of chocolate packets: "))  
arr = []
print("Enter each chocolate packet value (use 0 for empty):")
for _ in range(N):
    arr.append(int(input()))

# Process and Output
result = push_zeros_to_end(arr, N)
print("Final Output:")
print(*result)