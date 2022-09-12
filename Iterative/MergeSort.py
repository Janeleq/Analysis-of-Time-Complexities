def mSort(array):
    groupsize = 1 #start from groups of size 1
    while groupsize < len(array):
        mergeGroups(array, groupsize) #merge pairs of groups
        groupsize *= 2 #double the size of the group
    return array

def mergeGroups(array, groupsize):
    i = 0
    while i < len(array):
        j = i + 2 * groupsize
        array[i:j] = merge(array, i, groupsize)
        i = i + (2 * groupsize)

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