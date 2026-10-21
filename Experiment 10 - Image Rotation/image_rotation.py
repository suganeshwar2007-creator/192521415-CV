
import cv2
import matplotlib.pyplot as plt
from google.colab import files

# Upload an image
uploaded = files.upload()
filename = next(iter(uploaded))

# Read the image
image = cv2.imread(filename)

if image is None:
    raise ValueError("Error: Unable to read the image.")

# Convert image from BGR to RGB
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Rotate the image 90 degrees clockwise
rotated = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
rotated_rgb = cv2.cvtColor(rotated, cv2.COLOR_BGR2RGB)

# Display original and rotated images
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(image_rgb)
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(rotated_rgb)
plt.title("90-Degree Clockwise Rotation")
plt.axis("off")

plt.tight_layout()
plt.savefig("output.png")
plt.show()

# Save rotated image
cv2.imwrite("rotated_image.png", rotated)

# Download output files
files.download("output.png")
files.download("rotated_image.png")
