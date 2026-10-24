
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

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Convert to a binary image
_, binary = cv2.threshold(
    gray, 127, 255, cv2.THRESH_BINARY
)

# Create a structuring element (kernel)
kernel = cv2.getStructuringElement(
    cv2.MORPH_RECT, (5, 5)
)

# Apply dilation
dilated = cv2.dilate(binary, kernel, iterations=1)

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
plt.imshow(dilated, cmap="gray")
plt.title("Dilated Image")
plt.axis("off")

plt.tight_layout()
plt.savefig("output.png")
plt.show()

# Save output images
cv2.imwrite("binary_image.png", binary)
cv2.imwrite("dilated_image.png", dilated)

# Download output files
files.download("output.png")
files.download("binary_image.png")
files.download("dilated_image.png")
