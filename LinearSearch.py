import random, time

# Linear Search
# Good for small datasets
# Best case: 1, Worst Case: n, Average = (n+1)/2
# Big O: O(n) = n

# using while loop
def lSearch1(array, key):
    i = 0
    while i < len(array):
        if array[i] == key:
            return i
        i += 1
    return -1

# using for loop
def lSearch2(array, key):
    i = 0
    for i in range(len(array)):
        if array[i] == key:
            return i
    return -1

print("Starting Timer...")
start_time = time.time()
output = lSearch1([1,2,3,8,9], 3)
time_taken = time.time() - start_time
print(f"Execution Time: {time_taken}")
# print(f"Index Position: {output}")``
