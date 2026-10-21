
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

# Convert BGR to RGB for display
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Get image dimensions
height, width = image.shape[:2]

# Define three points in the original image
source_points = np.float32([
    [0, 0],
    [width - 1, 0],
    [0, height - 1]
])

# Define their new positions
destination_points = np.float32([
    [width * 0.1, height * 0.2],
    [width * 0.9, height * 0.1],
    [width * 0.2, height * 0.9]
])

# Calculate affine transformation matrix
matrix = cv2.getAffineTransform(
    source_points, destination_points
)

# Apply affine transformation
transformed = cv2.warpAffine(
    image, matrix, (width, height)
)

# Convert transformed image to RGB
transformed_rgb = cv2.cvtColor(
    transformed, cv2.COLOR_BGR2RGB
)

# Display original and transformed images
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(image_rgb)
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(transformed_rgb)
plt.title("Affine Transformed Image")
plt.axis("off")

plt.tight_layout()
plt.savefig("output.png")
plt.show()

# Save transformed image
cv2.imwrite("affine_transformed.png", transformed)

# Download output files
files.download("output.png")
files.download("affine_transformed.png")
