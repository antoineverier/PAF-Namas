# Importing Necessary Libraries
# Displaying the sample image - Monochrome Format
from skimage import data
from skimage import filters
from skimage.io import imshow, imread
from skimage.color import rgb2gray
import matplotlib.pyplot as plt

# Sample Image of scikit-image package
img = imread(r'C:\Users\Nina\Documents\Cours-TP\PAF\data\bras_lum.jpg')
gray_img = rgb2gray(img)

# Setting the plot size to 15,15
plt.figure(figsize=(15, 15))

for i in range(10):

  # Iterating different thresholds
  binarized_gray = (gray_img > i*0.1)*1
  plt.subplot(5,2,i+1)

  # Rounding of the threshold
  # value to 1 decimal point
  plt.title("Threshold: >"+str(round(i*0.1,1)))

  # Displaying the binarized image
  # of various thresholds
  plt.imshow(binarized_gray, cmap = 'gray')

plt.tight_layout()

plt.show()