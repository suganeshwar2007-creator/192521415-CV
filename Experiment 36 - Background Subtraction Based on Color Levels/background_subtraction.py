
import cv2
import numpy as np
import matplotlib.pyplot as plt
from google.colab import files

# Upload input image
uploaded = files.upload()
filename = next(iter(uploaded))

# Read image
img = cv2.imread(filename)

if img is None:
    raise ValueError("Image could not be loaded.")

# Function to subtract background based on color levels
def subtract_background(image, lower_color, upper_color):

    # Convert BGR image to HSV
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Identify background color range
    mask = cv2.inRange(hsv, lower_color, upper_color)

    # Invert mask to keep foreground
    foreground_mask = cv2.bitwise_not(mask)

    # Remove background
    result = cv2.bitwise_and(
        image, image, mask=foreground_mask
    )

    return result

# Define background color range (example: green)
lower = np.array([35, 40, 40])
upper = np.array([85, 255, 255])

# Apply background subtraction
output = subtract_background(img, lower, upper)

# Display original and output images
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(output, cv2.COLOR_BGR2RGB))
plt.title("Background Removed")
plt.axis("off")

plt.show()

# Save output
cv2.imwrite("background_removed.png", output)

# Download output
files.download("background_removed.png")
