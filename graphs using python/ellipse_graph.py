import matplotlib.pyplot as plt
import numpy as np

# define the ellipse parameters
a = 3 # semi-major axis
b = 2 # semi-minor axis
x0 = 1 # x-center
y0 = 1 # y-center

# generate some data 
t = np.linspace(0, 2*np.pi, 1000)
x = x0 + a*np.cos(t)
y = y0 + b*np.sin(t)

# create an ellipse graph
fig, ax = plt.subplots()
ax.plot(x, y)

# add labels and title
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Ellipse Graph')

# show the plot 
plt.show()