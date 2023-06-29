import numpy as np
import cv2

# Read the image
img = cv2.imread(r'C:\Users\Nina\Documents\Cours-TP\PAF\data\2_grains.jpg')

# Convert image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Perform thresholding
ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

# Find contours in the thresholded image
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# données
real_diameter = 25.75  # mm

# liste des diamètres pour déterminer le pièce de monnaie
piece = []

# Iterate over each contour
for contour in contours:
    # Calculate contour properties (area, perimeter, centroid, etc.)
    area = cv2.contourArea(contour)
    perimeter = cv2.arcLength(contour, True)
    moments = cv2.moments(contour)

    if moments['m00'] != 0:
        centroid_x = int(moments['m10'] / moments['m00'])
        centroid_y = int(moments['m01'] / moments['m00'])
    else:
        centroid_x = 0
        centroid_y = 0

    # Create a separate mask for the current contour
    contour_mask = np.zeros_like(gray)
    cv2.drawContours(contour_mask, [contour], 0, 255, -1)

    # Apply the mask to the original image to obtain the segmented region
    segmented_region = cv2.bitwise_and(img, img, mask=contour_mask)

    # Calculate the minimum enclosing circle for the contour
    (x, y), radius = cv2.minEnclosingCircle(contour)
    diameter = 2 * radius

    piece.append(diameter)

    # Display the segmented region
    cv2.imshow('Segmented Region', segmented_region)
    cv2.waitKey(0)

    ratio = real_diameter / np.max(piece)
    # conversion des caractéristiques en mm
    converted_area = area * (ratio**2)
    converted_diameter = diameter * ratio
    converted_perimeter = perimeter * ratio
    converted_centroid_x = centroid_x * ratio
    converted_centroid_y = centroid_y * ratio

    # Print contour properties
    print('Area (in mm²):', converted_area)
    print('Perimeter (in mm):', converted_perimeter)
    print('Centroid (in mm):', converted_centroid_x, converted_centroid_y)
    print('Diameter (in mm):', converted_diameter)
    print('-------------------------')




# Close all windows
cv2.destroyAllWindows()