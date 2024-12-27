# a decorator that accepts arguments to customize its behavior

def repeat(n):
    def decorator(func):
        def wrapper(*args,**kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f'hello,{name}')

greet("ram")