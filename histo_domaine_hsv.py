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

# Create the histogram in color space
bins = 64  # Number of bins for each color channel
histograms = []
combinations = [(0, 1), (1, 2), (0, 2)]  # Combinations of color channels to visualize
channel_names = ['Hue', 'Saturation', 'Value']  # Names for color channels

for channel1, channel2 in combinations:
    histogram, x_edges, y_edges = np.histogram2d(
        image_hsv[:, :, channel1].ravel(),
        image_hsv[:, :, channel2].ravel(),
        bins=bins,
        range=[(0, 1), (0, 1)]
    )
    histograms.append(histogram)

# Normalize the histograms for visualization
histograms = np.array(histograms)
histograms /= np.max(histograms)

# Plot the histograms as 2D heatmaps
fig, axs = plt.subplots(1, len(combinations), figsize=(15, 5))

for i, (channel1, channel2) in enumerate(combinations):
    axs[i].imshow(histograms[i], cmap='hot', origin='lower', extent=[0, 1, 0, 1])
    axs[i].set_xlabel(channel_names[channel1])
    axs[i].set_ylabel(channel_names[channel2])
    axs[i].set_title(f'Histogram ({channel_names[channel1]}, {channel_names[channel2]})')

plt.suptitle("Color Histogram (HSV)")
plt.tight_layout()
plt.show()