
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

# Convert BGR to RGB for displaying with Matplotlib
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Get original dimensions
height, width = image.shape[:2]
print("Original size:", width, "x", height)

# Resize to a bigger size (2x)
bigger = cv2.resize(
    image, None, fx=2, fy=2,
    interpolation=cv2.INTER_CUBIC
)

# Resize to a smaller size (half)
smaller = cv2.resize(
    image, None, fx=0.5, fy=0.5,
    interpolation=cv2.INTER_AREA
)

print("Bigger size:", bigger.shape[1], "x", bigger.shape[0])
print("Smaller size:", smaller.shape[1], "x", smaller.shape[0])

# Convert resized images to RGB
bigger_rgb = cv2.cvtColor(bigger, cv2.COLOR_BGR2RGB)
smaller_rgb = cv2.cvtColor(smaller, cv2.COLOR_BGR2RGB)

# Display all images
plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.imshow(image_rgb)
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 3, 2)
plt.imshow(bigger_rgb)
plt.title("Bigger Image (2x)")
plt.axis("off")

plt.subplot(1, 3, 3)
plt.imshow(smaller_rgb)
plt.title("Smaller Image (0.5x)")
plt.axis("off")

plt.tight_layout()
plt.savefig("output.png")
plt.show()

# Save resized images
cv2.imwrite("bigger_image.png", bigger)
cv2.imwrite("smaller_image.png", smaller)

# Download output files
files.download("output.png")
files.download("bigger_image.png")
files.download("smaller_image.png")
