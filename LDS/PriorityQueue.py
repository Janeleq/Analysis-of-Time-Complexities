        
class PriorityQueue(Queue):
    def __init__(self, order = "ascending"):
        self.array = []
        
        # value is True if its ascending order
        self.order = order
    
    def enqueue(self, item):
        self.array.append(item)
        
        # sort the array everytime something is enqueued, don't reverse if order is ascending
        self.array = sorted(self.array, reverse = self.order != "ascending")