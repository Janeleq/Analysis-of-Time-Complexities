# Python implementation of stack and queue
from hashlib import new
from inspect import stack
import threading
from queue import Queue as Q
from time import sleep
from tkinter import *
from tkinter import ttk


# Stack 
# LIFO property: last item placed on the stack will be the first item removed
# 3 primary operations: push, pop, peek
# push: places a new data element on the top of a stack; O(n) as require each element to shift by one position
# peek: inspects the data element on top of the stack without removing it; O(1) as simply access an array element by index
# pop: removes and retrieves the data element on top of the stack; O(n) as require each element to shift by one position

# Queue
# FIFO property
# 3 primary operations: enqueue, dequeue, peek
# Enqueue: places a new data element to tail of the queue; O(1) as we just insert an element at the end of the array
# Dequeue: removes data element at the head of queue; O(n) as require each element to shift by one position


# Stack & Recursion
# Stack can be used to create a non-recursive version of a recursion
class Stack:
    
    def __init__(self):
        self.array = []
    
    def push(self, item):
        self.array.append(item)
        
    def pop(self):
        if len(self.array) > 0:
            last = self.array[-1]
            self.array.pop()
            return last
        else:
            print("Stack is empty")
    
    def peek(self):
        if len(self.array) == 0:
            print("Stack is empty")
        else:
            return self.array[-1]
    
    def count(self):
        return len(self.array)
        
    def display(self):
        print(str(self.array) + " <= top")  

stack_obj = Stack()
stack_obj.array = [1, 4, 3]
print(stack_obj.peek())
        
        
# checks whether text contains balanced braces using stack
def check_braces(text):
    s = Stack()
    for ch in text:
        if ch == "{":
            s.push(ch) # push opening brace into stack
        elif ch == "}":
            if s.count() > 0: # ensure stack not empty when pop
                s.pop() # pop when closing brace encountered
            else:
                return False	# return False since stack is empty
    return s.count() == 0       # return True if stack is empty

# a list named li is used to contain data elements
# first element (index 0) is top of the stack
def push(li, item):
    li.insert(0,item)

# a list named li is used to contain data elements
# first element (index 0) is top of the stack
def pop(li):
    if len(li) > 0:
        item = li[0]
        del li[0]
        return item

# a list named li is used to contain data elements
# first element (index 0) is top of the stack
def peek(li):
    if len(li) > 0:
        return li[0]

def enqueue(li,item):
    li.append(item)

def dequeue(li):
    if len(li) > 0:
        item = li[0]
        del li[0]
        return item



        


            
# visualization classes and methods 
# thread class to draw the list
class Drawer(threading.Thread):
    def __init__(self, q):
        threading.Thread.__init__(self)
        self.daemon = True
        self.q = q
   
    def run(self):
        root = Tk()
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        canvas = Canvas(root)
        canvas.grid(column=0, row=0, sticky=(N, W, E, S))
        
        # inner method called update
        def update():
            canvas.delete('all')
            
            # gets item from the queue passed by the threads
            item = self.q.get(True)
            
            # gets array from the item
            list = item
            if type(item) != type([]):
                list = item.array
            
            # represents first block (to be coloured)
            first = None
            
            # the starting Y co-ordinate for the blocks
            startY = 10
            
            # assigns the relevant labels depending on the type of list
            if len(list) > 0:
                top = ""
                bottom = ""
                if type(item) == Stack:
                    item_name = "Stack"
                    top = "Top"
                    bottom = "Bottom"
                elif type(item) == Queue:
                    item_name = "Queue"
                    top = "Head"
                    bottom = "  Tail"
                elif type(item) == PriorityQueue:
                    item_name = "Priority queue"
                    top = "Head"
                    bottom = "  Tail"
                else:
                    item_name = "List"
                    top = "Top"
                    bottom = "Bottom"
                
                # adds the top text label
                label = canvas.create_text((38, startY), text=top, anchor='nw')
                startY += 20
                    
                # reverse the list if its a stack
                if type(item) is Stack:
                    list = list[::-1]
                    
                for e in list:
                    rectangle = canvas.create_rectangle((10, startY, 90, startY + 30))
                    label = canvas.create_text((48-2.2*len(str(e)), startY + 10), text=e, anchor='nw')
                    startY += 30
                    
                    # gets reference to top block
                    if first == None:
                        first = rectangle
                    
                # colour first block to be red
                canvas.itemconfig(first, fill='red')
                
                # adds the bottom text label
                startY += 5
                label = canvas.create_text((33, startY), text=bottom, anchor='nw')
                
            else:
                item_name = ""
                if type(item) == Stack:
                    item_name = "Stack"
                elif type(item) == Queue:
                    item_name = "Queue"
                elif type(item) == PriorityQueue:
                    item_name = "Priority queue"
                else:
                    item_name = "List"
                    
                label = canvas.create_text((20, startY), text= item_name + " is empty", anchor='nw')
            
            # reupdate the drawing thread
            root.after(100, update)

        # call the update method, and mainloop to keep this method running
        root.after(100, update)
        root.mainloop()

# thread class to update the list
class ListUpdater(threading.Thread):
    def __init__(self, list, q):
        self.thread = threading.Thread.__init__(self)
        self.daemon = True
        self.list = list
        self.q = q
    
    def run(self):
        # if drawing thread is terminated
        while True:
            if self.q.empty():
                self.q.put(self.list)
                
            # to set the list to update every half second
            sleep(0.5)
    
# method to create two threads for updating list and drawing list
def view_list(list, q = Q()):
    draw_thread = Drawer(q)
    update_thread = ListUpdater(list, q)
    draw_thread.start()
    update_thread.start()
    return

