# Recursive Merge Sort (Top-down Approach)

# Big O: O(nlogn)
# There are logn levels of recursion with decreasing group size size
# For each level, there are 2n/size recursion calls
# For each level, every pair of recursive function calls has a marge2 operation => each level has n/size calls to marge2
# Each merge2 operation conducts up to size comparisons in the worst case

def rmSort(a):
    if len(a) == 1:
        return a 
    mid = len(a)//2
    a1 = rmSort(a[0:mid])
    a2 = rmSort(a[mid:len(a)])
    return merge2(a1, a2)

def merge2(a1, a2):
    i = 0
    j = 0
    r = []
    while i < len(a1) or j < len(a2):
        if (j == len(a2)) or (i < len(a1) and a1[i] < a2[j]):
            r.append(a1[i]) #pick item from a1
            i += 1

        else:
            r.append(a2[j]) # pick item from a2
            j += 1
    return r

output = rmSort([1,3,2,70,55])
print(output)
