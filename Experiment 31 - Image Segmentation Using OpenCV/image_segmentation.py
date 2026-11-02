
import cv2
import matplotlib.pyplot as plt
from google.colab import files

# Step 1: Upload an image
uploaded = files.upload()
filename = next(iter(uploaded))

# Step 2: Read the input image
image = cv2.imread(filename)

if image is None:
    raise ValueError("Error: Unable to read the image.")

# Step 3: Convert image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Step 4: Set threshold values
lower_threshold = 100
upper_threshold = 200

# Step 5: Apply binary threshold segmentation
_, segmented = cv2.threshold(
    gray,
    lower_threshold,
    255,
    cv2.THRESH_BINARY
)

# Step 6: Apply inverse threshold segmentation
_, inverse_segmented = cv2.threshold(
    gray,
    lower_threshold,
    255,
    cv2.THRESH_BINARY_INV
)

# Step 7: Apply range-based segmentation
range_segmented = cv2.inRange(
    gray,
    lower_threshold,
    upper_threshold
)

# Step 8: Display the results
plt.figure(figsize=(14, 8))

plt.subplot(2, 2, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("Original Image")
plt.axis("off")

plt.subplot(2, 2, 2)
plt.imshow(gray, cmap="gray")
plt.title("Grayscale Image")
plt.axis("off")

plt.subplot(2, 2, 3)
plt.imshow(segmented, cmap="gray")
plt.title("Binary Segmentation")
plt.axis("off")

plt.subplot(2, 2, 4)
plt.imshow(range_segmented, cmap="gray")
plt.title("Threshold Range Segmentation")
plt.axis("off")

plt.tight_layout()
plt.savefig("output.png")
plt.show()

# Step 9: Save output images
cv2.imwrite("segmented_image.png", segmented)
cv2.imwrite("inverse_segmented.png", inverse_segmented)
cv2.imwrite("range_segmented.png", range_segmented)

# Step 10: Download results
files.download("output.png")
files.download("segmented_image.png")
files.download("inverse_segmented.png")
files.download("range_segmented.png")

print("Image segmentation completed successfully!")
