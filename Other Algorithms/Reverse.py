# A recursive algorithm reverse(a) that returns an array with the same elements as a, but in reverse order

# Worst case complexity: O(n)

# def reverse(a):
#     if len(a) == 1:
#         return a
#     else:
#         return [a[-1]] + reverse(a[:-1])
    
# print(reverse([1, 4, 3]))

def mystery(n):

   if n == 0:

     return 1

   else:
     if n%2 == 0:

        return mystery(n//2) + mystery(n//2)

     else:

        return mystery(n//2) * mystery(n//2)

print(mystery(20))