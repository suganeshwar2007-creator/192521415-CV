
import cv2
import matplotlib.pyplot as plt
from google.colab import files

# Upload the source image
uploaded = files.upload()
filename = next(iter(uploaded))

# Read the image
image = cv2.imread(filename)

if image is None:
    raise ValueError("Error: Unable to read the image.")

# Get image dimensions
height, width = image.shape[:2]

# Select the Region of Interest (ROI)
x1 = width // 4
y1 = height // 4
x2 = 3 * width // 4
y2 = 3 * height // 4

# Crop the ROI
roi = image[y1:y2, x1:x2]

# Copy the ROI
copied_roi = roi.copy()

# Paste the copied ROI into another location
result = image.copy()
roi_height, roi_width = copied_roi.shape[:2]

paste_x = 0
paste_y = 0

result[paste_y:paste_y + roi_height,
       paste_x:paste_x + roi_width] = copied_roi

# Convert images from BGR to RGB for display
original_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
roi_rgb = cv2.cvtColor(roi, cv2.COLOR_BGR2RGB)
result_rgb = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)

# Display the results
plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.imshow(original_rgb)
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 3, 2)
plt.imshow(roi_rgb)
plt.title("Cropped ROI")
plt.axis("off")

plt.subplot(1, 3, 3)
plt.imshow(result_rgb)
plt.title("Copied and Pasted ROI")
plt.axis("off")

plt.tight_layout()
plt.savefig("output.png")
plt.show()

# Save output images
cv2.imwrite("cropped_roi.png", roi)
cv2.imwrite("roi_result.png", result)

# Download output files
files.download("output.png")
files.download("cropped_roi.png")
files.download("roi_result.png")
