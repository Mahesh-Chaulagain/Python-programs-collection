# a fourth-order numerical method for solving ordinary differential equations(ODEs), more accurate than euler's method for
# many types of problems

def runge_kutta_4(func, initial_x, initial_y, step_size, num_steps):
    x = initial_x 
    y = initial_y
    for _ in range(num_steps):
        k1 = step_size * func(x, y)
        k2 = step_size * func(x + step_size/2, y + k1/2)
        k3 = step_size * func(x + step_size/2, y + k2/2)
        k4 = step_size * func(x + step_size, y + k3)
        y += (k1 + 2*k2 + 2*k3 + k4) / 6
        x += step_size
    return x, y

# example usuage
def dy_dx(x, y):
    return x + y

x_final, y_final =  runge_kutta_4(dy_dx, initial_x=0, initial_y=1, step_size=0.1, num_steps=100)
print(f"At x = {x_final}, y = {y_final}")