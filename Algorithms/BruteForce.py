# Brute Force Algorithm
# inputs: 2 non -ve integers a and b

def bruteForce(a,b):
    t = min(a,b)

    while(t != 1):
        if(a % t == 0 and b % t == 0):
            return t
        else:
            t = t -1

    return t

# print(bruteForce(81, 36))


def bruteForce2(sequence):

    product = 0

    for number in sequence:
        for i in range(0, len(sequence)):
            if(number == sequence[i]):
                continue
            check_product = number * sequence[i]
            if check_product > product:
                product = check_product
    return product

print(bruteForce2([5,6,2,8,4]))
    