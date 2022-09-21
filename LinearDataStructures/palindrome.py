# Stack and Queue Usage: Palindrome
def is_palindrome(word):
    s = Stack()
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