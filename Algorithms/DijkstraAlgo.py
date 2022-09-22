# Dijkstra's Algorithm 
# Calculate the greatest common divisor (GCD) of 2 integers using recursion
# Small number of operations compared to Brute Force Algo

# Iterative version
def dijkstra_iter(a,b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a

# Recursive version
# Complexity: O(n)
def dijkstra_recur(a,b):
    if a == b:
        return a
    elif a > b:
        return dijkstra_recur(a-b, b)
    else:
        return dijkstra_recur(a, b-a)
