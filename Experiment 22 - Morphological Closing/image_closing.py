
import cv2
import matplotlib.pyplot as plt
from google.colab import files

# Upload the input image
uploaded = files.upload()
filename = next(iter(uploaded))

# Read the image
image = cv2.imread(filename)

if image is None:
    raise ValueError("Error: Unable to read the image.")

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Convert to binary image
_, binary = cv2.threshold(
    gray, 127, 255, cv2.THRESH_BINARY
)

# Create a structuring element
kernel = cv2.getStructuringElement(
    cv2.MORPH_RECT, (5, 5)
)

# Apply morphological closing
closed = cv2.morphologyEx(
    binary, cv2.MORPH_CLOSE, kernel
)

# Display the results
plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 3, 2)
plt.imshow(binary, cmap="gray")
plt.title("Binary Image")
plt.axis("off")

plt.subplot(1, 3, 3)
plt.imshow(closed, cmap="gray")
plt.title("Closing Image")
plt.axis("off")

plt.tight_layout()
plt.savefig("output.png")
plt.show()

# Save output images
cv2.imwrite("binary_image.png", binary)
cv2.imwrite("closing_image.png", closed)

# Download output files
files.download("output.png")
files.download("binary_image.png")
files.download("closing_image.png")
