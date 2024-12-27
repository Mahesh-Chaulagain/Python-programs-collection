import matplotlib.pyplot as plt 
import numpy as np

# generate some data
x = np.linspace(0.01, 20, 100)
y = np.log(x)

# create a logarithm function graph
fig, ax = plt.subplots()
ax.plot(x, y)

# add labels and title
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Logarithm function Graph')

# show the plot
plt.show()