# a root-finding algorithm that uses a succession of roots of secant lines to better approximate a root of a function

def secant_method(func, x0, x1, tolerance=1e-10, max_iterations=100):
    for _ in range(max_iterations):
        fx1 = func(x1)
        if abs(fx1) < tolerance:
            return x1
        fx0 = func(x0)
        denominator = (fx1 - fx0) / (x1 - x0)
        x_next = x1 - fx1 / denominator
        x0, x1 = x1, x_next
    raise ValueError("Failed to coverage")

# example usuage
def g(x):
    return x**3 - 2*x - 5

root = secant_method(g, x0=2, x1=3)
print(f"Root found at x = {root}")