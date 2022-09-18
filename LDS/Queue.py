# Python implementation of queue

# Queue
# FIFO property
# 3 primary operations: enqueue, dequeue, peek
# Enqueue: places a new data element to tail of the queue
# Dequeue: removes data element at the head of queue

class Queue:
    
    def __init__(self):
        self.array = []
    
    def enqueue(self, item):
        self.array.append(item)
        
    def dequeue(self):
        if len(self.array) > 0:
            first = self.array[0]
            self.array = self.array[1:]
            return first
        else:
            print("Queue is empty")
    
    def peek(self):
        if len(self.array) == 0:
            print("Queue is empty")
        else:
            return self.array[0]

    def count(self):
        return len(self.array)

    def display(self):
        print("head => " + str(self.array))