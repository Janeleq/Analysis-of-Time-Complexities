import random, time #track the complexity of different functions

# Insertion sort
# Best case: O(n), Worst case: O(n^2)
# Big O: O(n^2)

def iSort(array, status):
    i = 1
    while i < len(array):
        # left of current element is all sorted; check against sorted and insert itself in the right position
        if(status in ["A", "a"]):
            move_left1(array, i)
        elif(status in ["D", "d"]):
            move_left2(array, i) 
        else:
            return "Sorry, please enter a valid sorting order (Ascending(A) / Descending(D))"
        i += 1
    return array

# Sorting in ascending order
def move_left1(array, i):
    while i > 0 and array[i] < array[i-1]:
        array[i], array[i-1] = array[i-1], array[i]
        i -= 1 

# Sorting in descending order
def move_left2(array, i):
    while i > 0 and array[i] > array[i-1]:
        array[i], array[i-1] = array[i-1], array[i]
        i -= 1

status = input("Do you want to sort in ascending(A) or descending(D) order?")

print("Starting timer..")
start_time = time.time()
print("Calling iSort function now...")
output = iSort([1, 4, 9, 10, 77, 88, 99], status) #  Best case for ascending, worst case for descending 
print(f"Output: {output}")
time_taken = time.time() - start_time
print(f"Execution time: {time_taken} seconds.") # display elapsed time 