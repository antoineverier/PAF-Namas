import numpy as np
import matplotlib.pyplot as plt
from skimage.segmentation import slic
from skimage.io import imshow, imread

# Charger l'image
image = imread(r'C:\Users\Nina\Documents\Cours-TP\PAF\data\bras_lum.jpg')

# Paramètres de l'algorithme SLIC
n_segments = 100    # Nombre de superpixels souhaité
compactness = 10    # Facteur de compacité (régule l'influence de la distance spatiale et de la similarité des couleurs)

# Appliquer l'algorithme SLIC pour segmenter l'image
segments = slic(image, n_segments=n_segments, compactness=compactness)

# Afficher l'image originale et les superpixels
fig, axes = plt.subplots(1, 2, figsize=(12, 6))
axes[0].imshow(image)
axes[0].set_title("Image originale")
axes[1].imshow(segments)
axes[1].set_title("Superpixels (SLIC)")
plt.tight_layout()
plt.show()