# a decorator to cache the results of expensive function calls

def cache(func):
    cached_results = {}
    def wrapper(*args):
        if args in cached_results:
            return cached_results[args]
        result = func(*args)
        cached_results[args] = result
        return result
    return wrapper

@cache
def slow_function(x):
    print(f"computing {x} ...")
    return x * x

print(slow_function(4))
print(slow_function(4))
print(slow_function(5))