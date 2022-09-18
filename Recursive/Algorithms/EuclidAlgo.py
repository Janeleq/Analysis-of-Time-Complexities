# Euclid's Algorithm
# Calculate the greatest common divisor (GCD) of 2 integers using recursion

# Iterative version
def euclid_iter(a,b):
    while b != 0:
        t = b
        b = a % b
        a = t
    return a

# Recursive version
def euclid_recur(a,b):
    if b == 0:
        return a
    else:
        return euclid_recur(b, a%b)