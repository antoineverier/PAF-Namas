import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imshow, imread
from skimage.color import rgb2gray
from skimage.exposure import equalize_hist
from skimage import img_as_ubyte

dark_image = imread(r'C:\Users\Nina\Documents\Cours-TP\PAF\data\testGrey.jpg')
plt.figure(num=None, figsize=(8, 6), dpi=80)
imshow(dark_image)

dark_image_grey = img_as_ubyte(rgb2gray(dark_image))
dark_image_eq = equalize_hist(dark_image_grey)

fig, axes = plt.subplots(1, 2, figsize=(15, 7))
axes[0].imshow(dark_image_grey, cmap='gray')
axes[0].set_title('Original Greyscale', fontsize=18)
axes[1].imshow(dark_image_eq, cmap='gray')
axes[1].set_title('Adjusted Greyscale', fontsize=18)

axes[0].axis('off')
axes[1].axis('off')

plt.show()