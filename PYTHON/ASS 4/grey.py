import numpy as np
import cv2
import matplotlib.pyplot as plt

# Function to convert RGB image to grayscale
def rgb_to_grayscale(image):
    # Use the weighted sum method to convert RGB to grayscale
    # Formula: 0.299 * R + 0.587 * G + 0.114 * B
    grayscale_image = 0.299 * image[:, :, 0] + 0.587 * image[:, :, 1] + 0.114 * image[:, :, 2]
    return grayscale_image.astype(np.uint8)

# Function to apply threshold to grayscale image
def apply_threshold(grayscale_image, threshold=128):
    # Apply threshold: if pixel value > threshold, set to 255 (white), else set to 0 (black)
    _, binary_image = cv2.threshold(grayscale_image, threshold, 255, cv2.THRESH_BINARY)
    return binary_image

# Example usage with a random RGB image
# Create a random RGB image with shape (height, width, 3)
# For example, 200x200 image with random RGB values
height, width = 200, 200
rgb_image = np.random.randint(0, 256, (height, width, 3), dtype=np.uint8)

# 1. Convert the RGB image to grayscale
grayscale_image = rgb_to_grayscale(rgb_image)

# 2. Apply threshold to convert the grayscale image to binary
binary_image = apply_threshold(grayscale_image, threshold=128)

# Display the results using matplotlib
plt.figure(figsize=(10, 5))

# Original RGB image
plt.subplot(1, 3, 1)
plt.imshow(rgb_image)
plt.title("Original RGB Image")
plt.axis('off')

# Grayscale image
plt.subplot(1, 3, 2)
plt.imshow(grayscale_image, cmap='gray')
plt.title("Grayscale Image")
plt.axis('off')

# Binary image
plt.subplot(1, 3, 3)
plt.imshow(binary_image, cmap='gray')
plt.title("Binary Image (Threshold Applied)")
plt.axis('off')

plt.show()
