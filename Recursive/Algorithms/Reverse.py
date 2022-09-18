# A recursive algorithm reverse(a) that returns an array with the same elements as a, but in reverse order

# Worst case complexity: O(n)

def reverse(a):
    if len(a) == 1:
        return a
    else:
        return [a[-1]] + reverse(a[:-1])
    
print(reverse([1, 4, 3]))