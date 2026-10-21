
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

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Create a kernel
kernel = np.ones((5, 5), np.uint8)

# Apply erosion
eroded = cv2.erode(gray, kernel, iterations=1)

# Display original and eroded images
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(gray, cmap="gray")
plt.title("Original Grayscale Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(eroded, cmap="gray")
plt.title("Eroded Image")
plt.axis("off")

plt.tight_layout()
plt.savefig("output.png")
plt.show()

# Save the eroded image
cv2.imwrite("eroded_image.png", eroded)

# Download output files
files.download("output.png")
files.download("eroded_image.png")
