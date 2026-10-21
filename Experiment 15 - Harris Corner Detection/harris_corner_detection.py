
import cv2
import numpy as np
import matplotlib.pyplot as plt
from google.colab import files

# Upload an image
uploaded = files.upload()
filename = next(iter(uploaded))

# Read the image
image = cv2.imread(filename)

if image is None:
    raise ValueError("Error: Unable to read the image.")

# Convert BGR image to RGB for display
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Convert image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Convert grayscale image to float32
gray_float = np.float32(gray)

# Apply Harris Corner Detection
harris = cv2.cornerHarris(
    gray_float,
    blockSize=2,
    ksize=3,
    k=0.04
)

# Dilate corner responses for better visibility
harris = cv2.dilate(harris, None)

# Mark detected corners in red
result = image.copy()
result[harris > 0.01 * harris.max()] = [0, 0, 255]

# Convert result to RGB for display
result_rgb = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)

# Display original and corner-detected images
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.imshow(image_rgb)
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(result_rgb)
plt.title("Harris Corner Detection")
plt.axis("off")

plt.tight_layout()
plt.savefig("output.png")
plt.show()

# Save detected corner image
cv2.imwrite("harris_corners.png", result)

# Download output files
files.download("output.png")
files.download("harris_corners.png")
