# -- Unsorted Array --
#   enqueue: O(1)
#   dequeue: O(n); require transversing whole array to find element with minimum value (highest priority)
#   peek: O(1)

# -- Sorted Array --
#   enqueue: O(n); in the worse case, iterate over all array positions to find a suitable position for a new element to remain sorted order
#   dequeue: O(1); elements stored in reverse sorted order/ if sorted order where smallest is in first position -> O(n)
#   peek: O(1)

# -- Binary Search Tree (average case) --
#   enqueue: O(logn)
#   dequeue: O(logn)
#   peek: O(1)

class PriorityQueue(Queue):
    def __init__(self, order = "ascending"):
        self.array = []
        
        # value is True if its ascending order
        self.order = order
    
    def enqueue(self, item):
        self.array.append(item)
        
        # sort the array everytime something is enqueued, don't reverse if order is ascending
        self.array = sorted(self.array, reverse = self.order != "ascending")