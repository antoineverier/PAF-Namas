import numpy as np
import cv2

# Read the images
img1 = cv2.imread(r'C:\Users\Nina\Documents\Cours-TP\PAF\data\test.jpg')
img2 = cv2.imread(r'C:\Users\Nina\Documents\Cours-TP\PAF\data\test2.jpg')

# Convert images to grayscale
gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# Perform thresholding
ret1, thresh1 = cv2.threshold(gray1, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
ret2, thresh2 = cv2.threshold(gray2, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

# Find contours in the thresholded images
contours1, hierarchy1 = cv2.findContours(thresh1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours2, hierarchy2 = cv2.findContours(thresh2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

color_similarities = []  # List to store color similarities

# Iterate over each contour in the first image
for contour1 in contours1:
    # Create a separate mask for the current contour in the first image
    contour_mask1 = np.zeros_like(gray1)
    cv2.drawContours(contour_mask1, [contour1], 0, 255, -1)

    # Apply the mask to the original image to obtain the segmented region in the first image
    segmented_region1 = cv2.bitwise_and(img1, img1, mask=contour_mask1)

    # Calculate the grayscale histogram for the segmented region in the first image
    hist1 = cv2.calcHist([segmented_region1], [0], None, [256], [0, 256])

    # Normalize the histogram
    hist1 /= hist1.sum()

    # Iterate over each contour in the second image
    for contour2 in contours2:
        # Create a separate mask for the current contour in the second image
        contour_mask2 = np.zeros_like(gray2)
        cv2.drawContours(contour_mask2, [contour2], 0, 255, -1)

        # Apply the mask to the original image to obtain the segmented region in the second image
        segmented_region2 = cv2.bitwise_and(img2, img2, mask=contour_mask2)

        # Calculate the grayscale histogram for the segmented region in the second image
        hist2 = cv2.calcHist([segmented_region2], [0], None, [256], [0, 256])

        # Normalize the histogram
        hist2 /= hist2.sum()

        # Calculate the histogram intersection between the two histograms
        intersection = cv2.compareHist(hist1, hist2, cv2.HISTCMP_INTERSECT)

        # Store the similarity measure (e.g., intersection) for comparison
        color_similarities.append(intersection)

# Calculate the average similarity measure
avg_similarity = np.mean(color_similarities)
print("Average similarity measure:", avg_similarity)
