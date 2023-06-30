import cv2
import numpy as np

img1 = cv2.imread(r'C:\Users\Nina\Documents\Cours-TP\PAF\data\test.jpg')
img2 = cv2.imread(r'C:\Users\Nina\Documents\Cours-TP\PAF\data\test7.jpg')


def calculate_texture_measures(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    texture_measures = {}

    # Calculate texture measures (variance, energy, entropy)
    variance = np.var(gray)
    energy = np.sum(gray.astype(np.float32) ** 2)
    entropy = -np.sum((gray / 255.0) * np.log2(gray / 255.0 + np.finfo(float).eps))

    texture_measures['variance'] = variance
    texture_measures['energy'] = energy
    texture_measures['entropy'] = entropy

    return texture_measures


