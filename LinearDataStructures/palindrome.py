#  Palindrome
# Stack and Queue Usage: Palindrome
from Stacks.Stack import StackOne
from Queue import Queue

# Using 1 Stack 1 Queue
def is_palindrome(word):
    s = StackOne()
    q = Queue()
    for ch in word:
        s.push(ch)
        q.enqueue(ch)
    while s.count() > 0:
        left = s.pop()
        right = q.dequeue()
        if left != right:
            return False
    return True

# Using a Stack 
def is_palindrome2(word):
    s = StackOne()
    n = len(word)
    mid = n//2
    for i in range(mid):
        s.push(word[i])
        s.push(word[n-1-i])

    while s.count()>0:
        c1 = s.pop()
        c2 = s.pop()
        if c1 != c2:
            return False
    return True

print(is_palindrome2("mamdam"))

# Using 2 queues
def is_palindrome3(word):
    q1 = Queue()
    q2 = Queue()

    n = len(word)
    mid = n//2
    for i in range(mid):
        q1.enqueue(word[i])
        q2.enqueue(word[n-1-i])

    while q1.count()>0:
        if q1.dequeue() != q2.dequeue():
            return False
    return True