"""WAP to create a decorator function which when applied to a function gives the execution time
of the function
"""
import time

def time_take(fxn):
   def inner_func(*args, **kwargs):
        start_time = time.time()
        result = fxn(*args, **kwargs)
        end_time = time.time()
        time_take = end_time - time_take
        return(fxn)
   return inner_func
# @time_decorater
def long_loop():
    for i in range(100000000):
        pass
start = time.time()
long_loop()
print("Taken time is", end-start)

# end = time.time()

import time
def execution_time_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Record the start time
        result = func(*args, **kwargs)  # Execute the function
        end_time = time.time()  # Record the end time
        execution_time = end_time - start_time  # Calculate the execution time
        print(f"Execution time of {func.__name__}: {execution_time:.6f} seconds")
        return result
    return wrapper

@execution_time_decorator
# def example_function():
def final_func():
    for _ in range(1000000):
        pass  # Simulating a time-consuming operation
result = final_func()   
print(final_func)

# example_function()

