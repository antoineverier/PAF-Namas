import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imshow, imread
from skimage.color import rgb2hsv, hsv2rgb
from skimage.exposure import equalize_hist

image = imread(r'C:\Users\Nina\Documents\Cours-TP\PAF\data\pied_lumnaturelle.jpg')

# Conversion RGB -> HSV
hsv_image = rgb2hsv(image)
hsv_image[:, :, 2] = equalize_hist(hsv_image[:, :, 2])
hsv_adjusted = hsv2rgb(hsv_image)

fig, ax = plt.subplots(1, 2, figsize=(15, 10))

ax[0].imshow(image)
ax[0].set_title('Original Image', fontsize=18)

ax[1].imshow(hsv_adjusted)
ax[1].set_title('HSV Adjusted Image', fontsize=18)

fig.tight_layout()
plt.show()



