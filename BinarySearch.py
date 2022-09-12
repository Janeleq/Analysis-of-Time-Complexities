import random, time

# Binary Search
# Good for big datasets; faster than Linear Search

def bSearch(array, target):
    lower = -1
    upper = len(array)

    while not (lower + 1 == upper):
        mid = (lower + upper) // 2
        if target == array[mid]:
            return mid
        elif target < array[mid]: # search lower region
            upper = mid
        else:
            lower = mid #search upper region

    return -1

print("Starting Timer...")
start_time = time.time()
output = bSearch([1,2,3,8,2], 8)
time_taken = time.time() - start_time
print(f"Execution Time: {time_taken}")
print(f"Index Position: {output}")