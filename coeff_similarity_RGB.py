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

R_similarities = []  # List to store R similarities
G_similarities = []  # List to store G similarities
B_similarities = []  # List to store B similarities

# Iterate over each contour in the first image
for contour1 in contours1:
    # Create a separate mask for the current contour in the first image
    contour_mask1 = np.zeros_like(gray1)
    cv2.drawContours(contour_mask1, [contour1], 0, 255, -1)

    # Apply the mask to the original image to obtain the segmented region in the first image
    segmented_region1 = cv2.bitwise_and(img1, img1, mask=contour_mask1)

    # Calculate the average RGB values for the segmented region in the first image
    avg_color1 = np.mean(segmented_region1, axis=(0, 1))

    # Iterate over each contour in the second image
    for contour2 in contours2:
        # Create a separate mask for the current contour in the second image
        contour_mask2 = np.zeros_like(gray2)
        cv2.drawContours(contour_mask2, [contour2], 0, 255, -1)

        # Apply the mask to the original image to obtain the segmented region in the second image
        segmented_region2 = cv2.bitwise_and(img2, img2, mask=contour_mask2)

        # Calculate the average RGB values for the segmented region in the second image
        avg_color2 = np.mean(segmented_region2, axis=(0, 1))

        # Calculate the color similarity for each component (R, G, B)
        R_similarity = abs(avg_color1[2] - avg_color2[2]) / 255.0
        G_similarity = abs(avg_color1[1] - avg_color2[1]) / 255.0
        B_similarity = abs(avg_color1[0] - avg_color2[0]) / 255.0

        R_similarities.append(R_similarity)
        G_similarities.append(G_similarity)
        B_similarities.append(B_similarity)

# Calculate the average color similarity for each component
avg_R_similarity = np.mean(R_similarities)
avg_G_similarity = np.mean(G_similarities)
avg_B_similarity = np.mean(B_similarities)

print('Average R Similarity:', avg_R_similarity)
print('Average G Similarity:', avg_G_similarity)
print('Average B Similarity:', avg_B_similarity)


# Close all windows
cv2.destroyAllWindows()