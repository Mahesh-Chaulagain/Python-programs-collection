from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from sklearn.cluster import KMeans

# Load image and scale it to [0, 255]
image = mpimg.imread('horses.jpg')
image = np.uint8(image * 255)  # Ensure pixel values are in [0, 255]

# Extract shape and reshape for KMeans
w, h, d = tuple(image.shape)
pixels = np.reshape(image, (w * h, d))

# Perform KMeans clustering to find dominant colors
n_colors = 10
model = KMeans(n_clusters=n_colors, random_state=42).fit(pixels)

# Get color palette (cluster centers) and convert to uint8
palette = np.uint8(model.cluster_centers_)

# Display the color palette
plt.imshow(palette.reshape(1, -1, 3))  # Reshape to a 1xN color strip
plt.axis('off')  # Optional: hide axis
plt.show()
