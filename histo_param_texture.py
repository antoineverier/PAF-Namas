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

# Calculate the measures for each grain of beauty
energies = []
entropies = []
variances = []

for grain_image in grain_images:
    grain_gray = cv2.cvtColor(grain_image, cv2.COLOR_BGR2GRAY)

    # Calculate energy, entropy, and variance for each grain of beauty
    energy = np.sum(np.square(grain_gray)) / grain_gray.size
    entropy = -np.sum(np.multiply(grain_gray / 255.0, np.log2(grain_gray / 255.0 + 1e-10)))
    variance = np.var(grain_gray)

    energies.append(energy)
    entropies.append(entropy)
    variances.append(variance)

# Calculate mean and standard deviation for each measure
mean_energy = np.mean(energies)
std_energy = np.std(energies)

mean_entropy = np.mean(entropies)
std_entropy = np.std(entropies)

mean_variance = np.mean(variances)
std_variance = np.std(variances)

# Plot the measures
x_labels = ['Grain 1', 'Grain 2', 'Grain 3', 'Grain 4', 'Grain 5', 'Grain 6', 'Grain 7']
x = np.arange(len(x_labels))

plt.figure(figsize=(10, 5))

plt.subplot(1, 3, 1)
plt.bar(x, energies, align='center')
plt.xticks(x, x_labels)
plt.xlabel('Grain of Beauty')
plt.ylabel('Energy')
plt.title('Energy for Each Grain of Beauty')

plt.subplot(1, 3, 2)
plt.bar(x, entropies, align='center')
plt.xticks(x, x_labels)
plt.xlabel('Grain of Beauty')
plt.ylabel('Entropy')
plt.title('Entropy for Each Grain of Beauty')

plt.subplot(1, 3, 3)
plt.bar(x, variances, align='center')
plt.xticks(x, x_labels)
plt.xlabel('Grain of Beauty')
plt.ylabel('Variance')
plt.title('Variance for Each Grain of Beauty')

plt.tight_layout()
plt.show()

# Print mean and standard deviation
print("Mean energy:", mean_energy)
print("Standard deviation of energy:", std_energy)

print("Mean entropy:", mean_entropy)
print("Standard deviation of entropy:", std_entropy)

print("Mean variance:", mean_variance)
print("Standard deviation of variance:", std_variance)
