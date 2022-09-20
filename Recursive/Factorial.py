# Reduction step = factorial(n) = n x factorial(n-1)
# Base case = factorial(1) = 1

# Time complexity: O(n)

# Space complexity: O(n)
# Max depth of recursion calls = n
def factorial(n):
    if n == 1: # 1 operation; O(n)
        return 1
    else:
        return n * factorial(n-1) 