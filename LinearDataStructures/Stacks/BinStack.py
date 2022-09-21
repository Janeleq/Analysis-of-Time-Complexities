def rbsearch(a, k, lower = None, upper = None):
    if lower == None:
        lower = -1
    if upper == None:
        upper = len(a)
    mid = (lower + upper) // 2
    if mid == lower:
        return -1
    if k == a[mid]:
        return mid
    if k < a[mid]:
        return rbsearch(a, k, lower, mid)
    if k > a[mid]:
        return rbsearch(a, k, mid, upper) 

def rbsearch_stack(a, k):
    lower = -1
    upper = len(a)
    s = Stack()
    s.push(lower)
    s.push(upper)
    
    while s.count() > 0:
        upper = s.pop()
        lower = s.pop()
        mid = (lower + upper) // 2
        if mid == lower:
            return -1
        if k == a[mid]:
            return mid 
        if k < a[mid]:
            s.push(lower)
            s.push(mid)
        if k > a[mid]:
            s.push(mid)
            s.push(upper)