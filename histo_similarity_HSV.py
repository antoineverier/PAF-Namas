import numpy as np
import cv2

# Read the images
img1 = cv2.imread(r'C:\Users\Nina\Documents\Cours-TP\PAF\data\test5.jpg')
img2 = cv2.imread(r'C:\Users\Nina\Documents\Cours-TP\PAF\data\test7.jpg')

# Convert images to HSV color space
hsv1 = cv2.cvtColor(img1, cv2.COLOR_BGR2HSV)
hsv2 = cv2.cvtColor(img2, cv2.COLOR_BGR2HSV)

# Perform thresholding on the value channel
_, _, v1 = cv2.split(hsv1)
_, _, v2 = cv2.split(hsv2)
ret1, thresh1 = cv2.threshold(v1, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
ret2, thresh2 = cv2.threshold(v2, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

# Find contours in the thresholded images
contours1, _ = cv2.findContours(thresh1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours2, _ = cv2.findContours(thresh2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

H_similarities = []  # List to store H similarities
S_similarities = []  # List to store S similarities
V_similarities = []  # List to store V similarities

# Iterate over each contour in the first image
for contour1 in contours1:
    # Create a separate mask for the current contour in the first image
    contour_mask1 = np.zeros_like(v1)
    cv2.drawContours(contour_mask1, [contour1], 0, 255, -1)

    # Apply the mask to the original image to obtain the segmented region in the first image
    segmented_region1 = cv2.bitwise_and(hsv1, hsv1, mask=contour_mask1)

    # Calculate the average HSV values for the segmented region in the first image
    avg_color1 = np.mean(segmented_region1, axis=(0, 1))

    # Iterate over each contour in the second image
    for contour2 in contours2:
        # Create a separate mask for the current contour in the second image
        contour_mask2 = np.zeros_like(v2)
        cv2.drawContours(contour_mask2, [contour2], 0, 255, -1)

        # Apply the mask to the original image to obtain the segmented region in the second image
        segmented_region2 = cv2.bitwise_and(hsv2, hsv2, mask=contour_mask2)

        # Calculate the average HSV values for the segmented region in the second image
        avg_color2 = np.mean(segmented_region2, axis=(0, 1))

        # Calculate the color similarity for each component (H, S, V)
        H_similarity = abs(avg_color1[0] - avg_color2[0]) / 180.0
        S_similarity = abs(avg_color1[1] - avg_color2[1]) / 255.0
        V_similarity = abs(avg_color1[2] - avg_color2[2]) / 255.0

        H_similarities.append(H_similarity)
        S_similarities.append(S_similarity)
        V_similarities.append(V_similarity)

# Calculate the average color similarity for each component
avg_H_similarity = np.mean(H_similarities)
avg_S_similarity = np.mean(S_similarities)
avg_V_similarity = np.mean(V_similarities)

print('Average H Similarity:', avg_H_similarity)
print('Average S Similarity:', avg_S_similarity)
print('Average V Similarity:', avg_V_similarity)


# Close all windows
cv2.destroyAllWindows()