# used for finding successfully better approximations to the roots(or zeroes) of a real-valued function

import numdifftools as nd

def newton_raphson(func, initial_guess, tolerance=1e-10, max_iterations=100):
    x0 = initial_guess
    for _ in range(max_iterations):
        fx0 = func(x0)
        if abs(fx0) < tolerance:
            return x0
        fprime_x0 = nd.Derivative(func)(x0)
        x0 = x0 - fx0 / fprime_x0
    raise ValueError("Failed to converge")

# example usuage
import math

def f(x):
    return x**3 - 2*x -5

root = newton_raphson(f, initial_guess=3)
print(f"root found at x = {root}")


# import scipy.misc

# def newton_raphson(func, initial_guess, tolerance=1e-10, max_iterations=100):
#     x0 = initial_guess
#     for _ in range(max_iterations):
#         fx0 = func(x0)
#         if abs(fx0) < tolerance:
#             return x0
#         fprime_x0 = scipy.misc.derivative(func, x0, dx=1e-6)  # Numerical differentiation
#         x0 = x0 - fx0 / fprime_x0
#     raise ValueError("Failed to converge")

# # Example usage
# def f(x):
#     return x**3 - 2*x - 5

# root = newton_raphson(f, initial_guess=3)
# print(f"Root found at x = {root}")

        
