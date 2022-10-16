from Stacks.Stack import StackOne

# Recursive Implementation of Dijkstra Algorithm
def dijkstra(a,b):
    if a == b:
        return a
    if a > b:
        return dijkstra(a-b, b)
    else:
        return dijkstra(a, b-a)

# Stack Implementation of Dijkstra Algorithm
def stk_dijkstra(a,b):
    stk = StackOne()
    stk.push(a)
    stk.push(b)
    while stk.count() > 0:
        b = stk.pop()
        a = stk.pop()

        if a == b:
            return a

        elif a > b:
            stk.push(a-b)
            stk.push(b)

        else:
            stk.push(a)
            stk.push(b-a)

        
