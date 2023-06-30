from skimage.io import imread, imsave
import matplotlib.pyplot as plt
try:
    from cStringIO import StringIO as BytesIO
except ImportError:
    from io import BytesIO

image_path = r'C:\Users\Nina\Documents\Cours-TP\PAF\data\test.jpg'

# Charger l'image
image = imread(image_path)

# Compression JPEG
compressed_image_path = image_path.replace('.jpg', '_compressed.jpg')
imsave(compressed_image_path, image, quality=75)

# Afficher l'image compressée
compressed_image = imread(compressed_image_path)
plt.imshow(compressed_image)
plt.axis('off')
plt.show()