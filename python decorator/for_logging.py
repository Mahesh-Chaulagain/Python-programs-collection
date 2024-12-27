# a decorator to log function calls and their arguments

def logger(func):
    def wrapper(*args, **kwargs):
        print(f"function {func.__name__} called with args:{args} and kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"function {func.__name__} returned {result}")
        return result
    return wrapper

@logger
def add(a, b):
    return a + b

add(3, 5)

@logger
def multiply(a, b, c):
    return a * b * c

multiply(2, 5, c=4)