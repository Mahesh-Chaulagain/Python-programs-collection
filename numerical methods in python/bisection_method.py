# a root finding algorithm that repeatedly bisects an interval and then selects a subinterval in which a root must
# lie for further processing

def bisection_method(func, a, b, tolerance=1e-10, max_iterations=100):
    if func(a) * func(b) >= 0:
        raise ValueError("Function does not change sign over interval")
    
    for _ in range(max_iterations):
        c = (a + b) / 2
        if abs(func(c)) < tolerance:
            return c
        if func(c) * func(a) < 0:
            b = c 
        else:
            a = c 
    raise ValueError("Failed to converge")

# example usuage
def h(x):
    return x**3 - 2*x - 5

root = bisection_method(h, a=2, b=3)
print(f"Root found at x = {root}")