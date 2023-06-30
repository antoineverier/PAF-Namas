import numpy as np
import cv2

# Read the images
img1 = cv2.imread(r'C:\Users\Nina\Documents\Cours-TP\PAF\data\test5.jpg')
img2 = cv2.imread(r'C:\Users\Nina\Documents\Cours-TP\PAF\data\test7.jpg')

# Convert images to Lab color space
lab1 = cv2.cvtColor(img1, cv2.COLOR_BGR2Lab)
lab2 = cv2.cvtColor(img2, cv2.COLOR_BGR2Lab)

# Perform thresholding on the a and b channels
_, a1, b1 = cv2.split(lab1)
_, a2, b2 = cv2.split(lab2)
ret1, thresh1 = cv2.threshold(a1, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
ret2, thresh2 = cv2.threshold(a2, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

# Find contours in the thresholded images
contours1, _ = cv2.findContours(thresh1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours2, _ = cv2.findContours(thresh2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

F_similarities = []  # List to store F similarities
a_similarities = []  # List to store a similarities
b_similarities = []  # List to store b similarities

# Iterate over each contour in the first image
for contour1 in contours1:
    # Create a separate mask for the current contour in the first image
    contour_mask1 = np.zeros_like(a1)
    cv2.drawContours(contour_mask1, [contour1], 0, 255, -1)

    # Apply the mask to the original image to obtain the segmented region in the first image
    segmented_region1 = cv2.bitwise_and(lab1, lab1, mask=contour_mask1)

    # Calculate the average Lab values for the segmented region in the first image
    avg_color1 = np.mean(segmented_region1, axis=(0, 1))

    # Iterate over each contour in the second image
    for contour2 in contours2:
        # Create a separate mask for the current contour in the second image
        contour_mask2 = np.zeros_like(a2)
        cv2.drawContours(contour_mask2, [contour2], 0, 255, -1)

        # Apply the mask to the original image to obtain the segmented region in the second image
        segmented_region2 = cv2.bitwise_and(lab2, lab2, mask=contour_mask2)

        # Calculate the average Lab values for the segmented region in the second image
        avg_color2 = np.mean(segmented_region2, axis=(0, 1))

        # Calculate the color similarity for each component (F, a, b)
        F_similarity = abs(avg_color1[0] - avg_color2[0]) / 100.0
        a_similarity = abs(avg_color1[1] - avg_color2[1]) / 128.0
        b_similarity = abs(avg_color1[2] - avg_color2[2]) / 128.0

        F_similarities.append(F_similarity)
        a_similarities.append(a_similarity)
        b_similarities.append(b_similarity)

# Calculate the average color similarity for each component
avg_F_similarity = np.mean(F_similarities)
avg_a_similarity = np.mean(a_similarities)
avg_b_similarity = np.mean(b_similarities)

print('Average F Similarity:', avg_F_similarity)
print('Average a Similarity:', avg_a_similarity)
print('Average b Similarity:', avg_b_similarity)

# Close all windows
cv2.destroyAllWindows()