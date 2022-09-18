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

print(bruteForce(81, 36))