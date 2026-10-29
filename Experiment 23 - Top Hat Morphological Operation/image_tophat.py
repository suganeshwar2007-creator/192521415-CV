
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

# Create a structuring element
kernel = cv2.getStructuringElement(
    cv2.MORPH_RECT, (5, 5)
)

# Apply Top-Hat operation
tophat = cv2.morphologyEx(
    gray, cv2.MORPH_TOPHAT, kernel
)

# Display the results
plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 3, 2)
plt.imshow(gray, cmap="gray")
plt.title("Grayscale Image")
plt.axis("off")

plt.subplot(1, 3, 3)
plt.imshow(tophat, cmap="gray")
plt.title("Top-Hat Image")
plt.axis("off")

plt.tight_layout()
plt.savefig("output.png")
plt.show()

# Save output images
cv2.imwrite("grayscale_image.png", gray)
cv2.imwrite("tophat_image.png", tophat)

# Download output files
files.download("output.png")
files.download("grayscale_image.png")
files.download("tophat_image.png")
