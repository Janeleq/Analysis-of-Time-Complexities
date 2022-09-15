# Base case: n = 0 / fibonacci(0)
#            n = 1 / fibonacci(1)

# Reduction step: n > 1
#                   fibonacci(n-1) + fibonacci(n-2)

# No of additions for fibonacci(n) = no of additions for fibonacci(n-1) + no of additions for fibonacci(n-2)+1
# Worst case complexity: O(2^n)
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)