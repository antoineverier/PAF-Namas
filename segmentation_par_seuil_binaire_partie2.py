import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imshow, imread
from skimage.color import rgb2gray

# Charger l'image
coffee = imread(r'C:\Users\Nina\Documents\Cours-TP\PAF\data\bras_lum.jpg')
gray_coffee = rgb2gray(coffee)

# Seuil à utiliser pour supprimer la zone
seuil = 0.7

# Binarisation de l'image
binarized_gray = (gray_coffee > seuil) * 1

# Trouver les coordonnées des pixels à supprimer
row_indices, col_indices = np.where(binarized_gray == 0)

# Créer une copie de l'image originale
region_of_interest = np.copy(coffee)

# Supprimer la zone en la remplaçant par une valeur spécifique
region_of_interest[row_indices, col_indices] = 255  # Remplacer par la valeur maximale (blanc)

# Afficher l'image originale et la région d'intérêt
fig, axes = plt.subplots(1, 2, figsize=(12, 6))
axes[0].imshow(coffee)
axes[0].set_title("Image originale")
axes[1].imshow(region_of_interest)
axes[1].set_title("Région d'intérêt (zone supprimée)")
plt.tight_layout()
plt.show()