# Merge Sort (Bottom-up approach)
# Big O: O(nlogn)
# Group Size (GS) = 1 at first level; doubles at each successive level
# After k steps, we cover an array of size 2^k = n ; No of steps k = logn
# Total number of elements per level = n
# Takes logn levels to go from n group size of 1 to a group size of n
# Total no of steps = no of levels x no of steps at each level = logn x n
# No of pairs to be merge at level g = n/(2*g)
# No of groups in specific level g = n/gs => say n = 8 and gs = 2 => we know there are 4 groups in the second level

# Iterate over increasing group sizes
def mSort(array):
    groupsize = 1 #start from groups of size 1
    while groupsize < len(array):
        mergeGroups(array, groupsize) #merge pairs of groups
        groupsize *= 2 #double the size of the group
    return array

# Iterate over pairs of groups of a given size
def mergeGroups(array, groupsize):
    i = 0
    while i < len(array):
        j = i + 2 * groupsize
        array[i:j] = merge(array, i, groupsize)
        i = i + (2 * groupsize)

# Iterate over items in each pair of groups
# Worst case: (2*g )
# For group size gs, max number of moves = 2 x gs
def merge(array, i ,groupsize):
    resultArray = [] #new array to store merged result
    firstGroup = array[i:i+groupsize] #end of first group
    secondGroup = array[i+groupsize:i+groupsize*2] #end of second group
    while (len(firstGroup) != 0 or len(secondGroup) != 0):
        if(len(firstGroup) == 0):
            while (len(secondGroup) != 0):
                resultArray.append(secondGroup.pop(0))
        elif (len(secondGroup) == 0):
            while (len(firstGroup) != 0):
                resultArray.append(firstGroup.pop(0))
        else:
            if(firstGroup[0] > secondGroup[0]):
                resultArray.append(secondGroup.pop(0))
            else:
                resultArray.append(firstGroup.pop(0))
    return resultArray
        
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
    ret = []
    while i < len(a1) or j < len(a2):
        if (j == len(a2)) or (i < len(a1) and a1[i] < a2[j]):
            ret.append(a1[i]) # pick item from 1st group
            i += 1
        else:
            ret.append(a2[j]) # pick item from 2nd group
            j += 1
    return ret