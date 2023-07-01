from skimage.io import imread
import matplotlib.pyplot as plt
try:
    from cStringIO import StringIO as BytesIO
except ImportError:
    from io import BytesIO


    im = generate_image(imread("C:/Users/02bar/Documents/TELECOM/PAF/Appareil de Macha/pied_lumdujour_zoome.jpg"))
    out = BytesIO()
    im.save(out, format=format,quality=75)
    out.seek(0)
    
    compressed_image = plt.imread(out)
    plt.imshow(compressed_image)
    plt.axis('off')
    plt.show()



