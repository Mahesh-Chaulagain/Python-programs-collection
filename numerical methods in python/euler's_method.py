# a first order numerical procedure for solving ordinary differential equations(ODEs)

def euler_method(func, initial_x, initial_y, step_size, num_steps):
    x = initial_x
    y = initial_y
    for _ in range(num_steps):
        y += step_size * func(x, y)
        x += step_size
    return x, y

# example usuage
def dy_dx(x, y):
    return x + y

x_final, y_final = euler_method(dy_dx, initial_x=0, initial_y=1, step_size=0.1, num_steps=100)
print(f"At x={x_final}, y={y_final}")