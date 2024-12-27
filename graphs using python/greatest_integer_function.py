import matplotlib.pyplot as plt
import numpy as np

# define the greatest integer function 
def greatest_integer(x):
    return np.floor(x)

# generate some data
x = np.linspace(-5, 5, 1000)
y = greatest_integer(x)

# create a greatest integer graph
fig, ax = plt.subplots()
ax.plot(x, y)

# add labels and a title
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title("Greatest Integer Graph")

# show the plot
plt.show()