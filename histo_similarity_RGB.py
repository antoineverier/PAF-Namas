import numpy as np
import cv2
import matplotlib.pyplot as plt

# Read the query image
query_image = cv2.imread(r'C:\Users\Nina\Documents\Cours-TP\PAF\data\test2.jpg')
query_gray = cv2.cvtColor(query_image, cv2.COLOR_BGR2GRAY)

# Read and process the grain of beauty images
grain_images = [
    cv2.imread(r'C:\Users\Nina\Documents\Cours-TP\PAF\data\test.jpg'),
    cv2.imread(r'C:\Users\Nina\Documents\Cours-TP\PAF\data\test3.jpg'),
    cv2.imread(r'C:\Users\Nina\Documents\Cours-TP\PAF\data\test4.jpg'),
    cv2.imread(r'C:\Users\Nina\Documents\Cours-TP\PAF\data\test5.jpg'),
    cv2.imread(r'C:\Users\Nina\Documents\Cours-TP\PAF\data\test6.jpg'),
    cv2.imread(r'C:\Users\Nina\Documents\Cours-TP\PAF\data\test7.jpg'),
    cv2.imread(r'C:\Users\Nina\Documents\Cours-TP\PAF\data\test8.jpg')
]

# Calculate the mean RGB values for each grain of beauty
mean_rgb_values = []

for grain_image in grain_images:
    grain_gray = cv2.cvtColor(grain_image, cv2.COLOR_BGR2GRAY)

    # Perform thresholding
    ret, thresh = cv2.threshold(grain_gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    # Find contours in the thresholded image
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Iterate over each contour
    contour_mask = np.zeros_like(grain_image)
    cv2.drawContours(contour_mask, contours, -1, (255, 255, 255), thickness=cv2.FILLED)

    # Apply the mask to the original image to obtain the segmented region
    segmented_region = cv2.bitwise_and(grain_image, contour_mask)

    # Calculate the mean RGB values for the segmented region
    mean_rgb = np.mean(segmented_region, axis=(0, 1))

    mean_rgb_values.append(mean_rgb)

# Convert the mean RGB values to numpy array
mean_rgb_values = np.array(mean_rgb_values)

# Calculate mean and standard deviation for each channel
mean_r = np.mean(mean_rgb_values[:, 0])
std_r = np.std(mean_rgb_values[:, 0])

mean_g = np.mean(mean_rgb_values[:, 1])
std_g = np.std(mean_rgb_values[:, 1])

mean_b = np.mean(mean_rgb_values[:, 2])
std_b = np.std(mean_rgb_values[:, 2])

# Plot the mean RGB values and histograms for each grain
x_labels = ['Grain 1', 'Grain 2', 'Grain 3', 'Grain 4', 'Grain 5', 'Grain 6', 'Grain 7']
x = np.arange(len(x_labels))

plt.figure(figsize=(15, 5))

# Plot for Mean Red
plt.subplot(1, 4, 1)
plt.bar(x, mean_rgb_values[:, 0], align='center', color='red')
plt.xticks(x, x_labels)
plt.xlabel('Grain of Beauty')
plt.ylabel('Mean Red')
plt.title('Mean Red Value for Each Grain of Beauty')

# Plot for Mean Green
plt.subplot(1, 4, 2)
plt.bar(x, mean_rgb_values[:, 1], align='center', color='green')
plt.xticks(x, x_labels)
plt.xlabel('Grain of Beauty')
plt.ylabel('Mean Green')
plt.title('Mean Green Value for Each Grain of Beauty')

# Plot for Mean Blue
plt.subplot(1, 4, 3)
plt.bar(x, mean_rgb_values[:, 2], align='center', color='blue')
plt.xticks(x, x_labels)
plt.xlabel('Grain of Beauty')
plt.ylabel('Mean Blue')
plt.title('Mean Blue Value for Each Grain of Beauty')



plt.tight_layout()
plt.show()

# Print mean and standard deviation
print("Mean Red:", mean_r)
print("Standard deviation of Red:", std_r)

print("Mean Green:", mean_g)
print("Standard deviation of Green:", std_g)

print("Mean Blue:", mean_b)
print("Standard deviation of Blue:", std_b)
