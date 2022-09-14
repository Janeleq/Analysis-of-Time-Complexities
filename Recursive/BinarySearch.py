# Recursive Binary Search

def rbsearch(array, target, lower=None, upper=None):
    if lower == None:
        lower = - 1
        upper = len(array)

    if lower + 1 == upper: # base case
        return -1           # not found

    mid = (lower + upper)//2
    if array[mid] == target: # base case
        return mid          # success
    elif array[mid] < target: # search upper region
        return rbsearch(array, target, mid, upper)
    else:                      # search lower region 
        return rbsearch(array, target, lower, mid)


output = rbsearch([1,4,3,88,38], 1)
print(output)