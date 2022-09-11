import random, time #track the complexity of different functions

#insertion sort
def iSort(array, status):
    i = 1
    while i < len(array):
        #left of current element is all sorted; check against sorted and insert itself in the right position
        if(status in ["A", "a"]):
            move_left1(array, i)
        elif(status in ["D", "d"]):
            move_left2(array, i) 
        else:
            return "Sorry, please enter a valid sorting order (Ascending(A) / Descending(D))"
        i += 1
    return array

#for sorting in ascending order
def move_left1(array, i):
    while i > 0 and array[i] < array[i-1]:
        array[i], array[i-1] = array[i-1], array[i]
        i -= 1 

#for sorting in descending order
def move_left2(array, i):
    while i > 0 and array[i] > array[i-1]:
        array[i], array[i-1] = array[i-1], array[i]
        i -= 1

status = input("Do you want to sort in ascending(A) / descending(D) order?")

print("Starting timer..")
start_time = time.time()
print("Calling iSort function now...")
output = iSort([1, 4, 9, 0, 77, 8, 99], status)
print(f"Output: {output}")
time_taken = time.time() - start_time
print(f"Execution time: {time_taken} seconds.") #display elapsed time for function