# Given a list of numbers in a pascal triangle
#            1
#        1       1 
#    1       2       1
# 1       3       3      1

# k is the kth number on level n in the pascal triangle
def pt(n, k):
    #base case 1
    if k == 1:
        return 1
    elif k == n - 1:
        return 1
    return pt(n-1, k-1) + pt(n-1, k)

