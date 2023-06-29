import numpy as np
import matplotlib.pyplot as plt
from skimage import util
from skimage import data
from skimage.color import rgb2gray, rgb2hsv
from skimage import io

# read original image, in full color
image = io.imread(r'C:\Users\Nina\Documents\Cours-TP\PAF\data\test.jpg')

# Convert image to HSV color space
image_hsv = rgb2hsv(image)

# Display the image
fig, ax = plt.subplots()
plt.imshow(image)

# Tuple to select colors of each channel line
colors = ("orange", "purple", "black")

# Create the histogram plot, with three lines, one for each color
plt.figure()
plt.xlim([0, 1])  # Range for HSV color space is [0, 1]
for channel_id, color in enumerate(colors):
    histogram, bin_edges = np.histogram(
        image_hsv[:, :, channel_id], bins=256, range=(0, 1)
    )
    plt.plot(bin_edges[0:-1], histogram, color=color)

plt.title("Color Histogram (HSV)")
plt.xlabel("Color value")
plt.ylabel("Pixel count")

plt.show()