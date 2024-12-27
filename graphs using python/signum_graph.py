import matplotlib.pyplot as plt 
import numpy as np

# define the signum function
def signum(x):
    if x > 0:
        return 1
    elif x == 0:
        return 0 
    else:
        return -1
    
# generate some data
x = np.linspace(-5, 5, 1000)
y = [signum(i) for i in x]

# create a signum graph
fig, ax = plt.subplots()
ax.plot(x, y)

# add labels and a title
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Signum Graph')

# show the plot
plt.show()
