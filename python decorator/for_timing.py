# a decorator to measure the execution time of a function

import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} executed in {end_time - start_time} seconds")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(2)
    return "finished"

print(slow_function())

@timer
def sample_time():
    time.sleep(4)
    return "slow"

print(sample_time())