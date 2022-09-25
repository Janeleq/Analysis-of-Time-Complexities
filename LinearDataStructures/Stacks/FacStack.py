from Stack import StackOne

def factorial(n):
    s = StackOne()
    s.push(n)
    result = 1

    while s.count() > 0:
        m = s.pop()
        result *= m
        if m > 1:
            s.push(m-1)

    return result

print(factorial(4))