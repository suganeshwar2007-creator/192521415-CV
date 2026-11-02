
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

# Function to subtract foreground based on color levels
def subtract_foreground(image, lower_color, upper_color):

    # Convert BGR image to HSV
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Detect foreground color range
    mask = cv2.inRange(hsv, lower_color, upper_color)

    # Invert mask to select background
    background_mask = cv2.bitwise_not(mask)

    # Remove foreground
    result = cv2.bitwise_and(
        image, image, mask=background_mask
    )

    return result

# Define foreground color range (example: red)
lower = np.array([0, 100, 100])
upper = np.array([10, 255, 255])

# Apply foreground subtraction
output = subtract_foreground(img, lower, upper)

# Display original and output images
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(output, cv2.COLOR_BGR2RGB))
plt.title("Foreground Removed")
plt.axis("off")

plt.show()

# Save output image
cv2.imwrite("foreground_removed.png", output)

# Download output
files.download("foreground_removed.png")
