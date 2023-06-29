import numpy as np
# import matplotlib.pyplot as plt
#
# import ipympl
# import imageio.v3 as iio
# import skimage
# import skimage.draw
# from skimage import io
#
# from skimage import data
# from skimage.color import rgb2gray
# from skimage import io
#

import matplotlib.pyplot as plt
from skimage import util
from skimage import data
from skimage.color import rgb2gray
from skimage import io



# # read the image of a plant seedling as grayscale from the outset
image = io.imread(r'C:\Users\Nina\Documents\Cours-TP\PAF\data\test.jpg')
#
#
# # read the image of a plant seedling as grayscale from the outset
#plant_seedling = iio.imread(uri="data/plant-seedling.jpg", mode="L")
#
# # convert the image to float dtype with a value range from 0 to 1
image_float = util.img_as_float(image)
#
# # display the image
fig, ax = plt.subplots()
# plt.imshow(image)
#
# # create the histogram
histogram, bin_edges = np.histogram(image_float, bins=256, range=(0, 1))
#
# # configure and draw the histogram figure
plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("grayscale value")
plt.ylabel("pixel count")
plt.xlim([0.0, 1.0])  # <- named arguments do not work here

plt.plot(bin_edges[0:-1], histogram)  # <- or here

plt.show()