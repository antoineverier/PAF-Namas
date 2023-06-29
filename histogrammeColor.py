

import numpy as np


import matplotlib.pyplot as plt
from skimage import util
from skimage import data
from skimage.color import rgb2gray
from skimage import io


# read original image, in full color
image = io.imread(r'C:\Users\Nina\Documents\Cours-TP\PAF\data\test.jpg')


# display the image
fig, ax = plt.subplots()
plt.imshow(image)

# tuple to select colors of each channel line
colors = ("red", "green", "blue")

# create the histogram plot, with three lines, one for
# each color
plt.figure()
plt.xlim([0, 256])
for channel_id, color in enumerate(colors):
    histogram, bin_edges = np.histogram(
        image[:, :, channel_id], bins=256, range=(0, 256)
    )
    plt.plot(bin_edges[0:-1], histogram, color=color)

plt.title("Color Histogram")
plt.xlabel("Color value")
plt.ylabel("Pixel count")

plt.show()