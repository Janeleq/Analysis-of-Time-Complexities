# A recursive algorithm sum(n) that computes the sum of the first n positive integers. For example, 
# sum(1) returns 1, sum(2) returns 1+2, sum(3) returns 1+2+3. 

# Worst case complexity: O(n)

def sum(n):
    str_num = str(n)

    if len(str_num) == 1:
        return int(str_num)

    else:
        str_num = str(n)
        return int(str_num[0]) + sum(int(str_num[1:len(str_num)]))

print(sum(6143))