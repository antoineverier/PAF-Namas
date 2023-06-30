import matplotlib.pyplot as plt

from skimage import data
from skimage.color import rgb2gray
from skimage import io

image = io.imread(r'C:\Users\Nina\Documents\Cours-TP\PAF\data\test2.jpg')


original = image
grayscale = rgb2gray(original)

fig, axes = plt.subplots(1, 2, figsize=(8, 4))
ax = axes.ravel()

ax[0].imshow(original)
ax[0].set_title("Original")
ax[1].imshow(grayscale, cmap=plt.cm.gray)
ax[1].set_title("Grayscale")

fig.tight_layout()


plt.show()