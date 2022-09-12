import random, time
from line_profiler import LineProfiler
# Binary Search
# Good for big datasets; faster than Linear Search
# Best Case: 1, Worst Case: logN + 1 
# Big O: O(logN)

# Use Line_Profiler Python Library to profile a function

def profile(func):
    def inner(*args, **kwargs):
        profiler.add_function(func)
        profiler.enable_by_count()
        return func(*args, **kwargs)
    return inner

def print_stats():
    profiler.print_stats()


@profile
def bSearch(array, target):
    lower = -1
    upper = len(array)

    while not (lower + 1 == upper):
        mid = (lower + upper) // 2
        if target == array[mid]:
            return mid
        elif target < array[mid]: # search lower region
            upper = mid
        else:
            lower = mid #search upper region
    return -1

profiler = LineProfiler()
lp_wrapper = profiler(bSearch)
lp_wrapper([1,2,3,4,6,5], 3)
profiler.print_stats()

# print("Starting Timer...")
# start_time = time.time()
# time_taken = time.time() - start_time
# print(f"Execution Time: {time_taken}")
