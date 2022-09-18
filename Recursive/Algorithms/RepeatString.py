# A Recursive algorithm repeat_string(s,n) that returns a concatenation of n copies of the string s. 
# For example, repeat_string("apple", 3) will return "appleappleapple".

# Worst case complexity: O(n)

def repeat_string(s,n):
    if n == 1:
        return s
    else:
        return s + repeat_string(s, n-1)

print(repeat_string("apple", 3))