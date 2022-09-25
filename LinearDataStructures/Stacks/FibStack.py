from Stack import StackOne
# Stack replacing recursive version of fibonacci
# 1. Create a new stack
# 2. Push initial parameters onto a stack
# 3. Iterate till stack is empty (pop parameter from stack, if base case dont push anymore, else push onto the stack parameters used in recurson)
def fibonacci_stack(n):
    s = StackOne()
    s.push(n)
    result = 0
    while s.count() > 0:
        s.display()
        current = s.pop()
        if current == 0:
            result += 0
        elif current == 1:
            result += 1
        else:
            s.push(current - 2)
            s.push(current - 1)
    
    return result

# Recursive version of Fibonacci
def fibonacci(n):
    print(n) # Show value at each step
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)