import matplotlib.pyplot as plt
import numpy as np

# generate some data
x = np.linspace(-5, 15, 100)
y = np.exp(x)

# create an exponential function graph
fig, ax = plt.subplots()
ax.plot(x, y)

# add labels and a title
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Exponential Function Graph')

# show the plot
plt.show()