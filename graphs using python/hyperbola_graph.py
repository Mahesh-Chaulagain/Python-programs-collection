import matplotlib.pyplot as plt
import numpy as np

# generate some data
x = np.linspace(-20, 20, 500)
y1 = np.sqrt(x**2 -1)
y2 = -np.sqrt(x**2 -1)

# create a hyperbola graph
fix, ax  = plt.subplots()
ax.plot(x, y1, color='blue', label='y = +sqrt(x^2 -1)')
ax.plot(x, y2, color='red', label='y = -sqrt(x^2 -1)')

# add labels and a title
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Hyperbola Graph')
ax.legend()

# show the plot 
plt.show()