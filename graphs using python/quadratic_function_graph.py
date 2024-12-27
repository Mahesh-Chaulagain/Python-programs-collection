import matplotlib.pyplot as plt
import numpy as np

# define the quadratic function
def quardatic(x, a, b, c):
    return a*x**2 + b*x +c

# generate some data
x = np.linspace(-10, 10, 1000)
y = quardatic(x, 4, 2, 1)

# create a quadratic graph
fix, ax = plt.subplots()
ax.plot(x, y)

# add labels and a title
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Quadratic Graph')

# show the plot
plt.show()
