
import cv2
import matplotlib.pyplot as plt
from google.colab import files

# Upload the original image
uploaded = files.upload()
filename = next(iter(uploaded))

# Read the image
image = cv2.imread(filename)

if image is None:
    raise ValueError("Error: Unable to read the image.")

# Create a copy for adding the watermark
watermarked = image.copy()
overlay = image.copy()

# Watermark text
text = "Copyright"

# Set font and size according to image dimensions
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = max(image.shape[1] / 800, 0.5)
thickness = 2

# Calculate watermark position (bottom-right)
text_size, baseline = cv2.getTextSize(
    text, font, font_scale, thickness
)

x = image.shape[1] - text_size[0] - 20
y = image.shape[0] - 20

# Add watermark to overlay
cv2.putText(
    overlay, text, (x, y), font, font_scale,
    (255, 255, 255), thickness, cv2.LINE_AA
)

# Blend overlay with original image
alpha = 0.4
watermarked = cv2.addWeighted(
    overlay, alpha, image, 1 - alpha, 0
)

# Convert images from BGR to RGB for display
original_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
watermarked_rgb = cv2.cvtColor(
    watermarked, cv2.COLOR_BGR2RGB
)

# Display original and watermarked images
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.imshow(original_rgb)
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(watermarked_rgb)
plt.title("Watermarked Image")
plt.axis("off")

plt.tight_layout()
plt.savefig("output.png")
plt.show()

# Save watermarked image
cv2.imwrite("watermarked_image.png", watermarked)

# Download output files
files.download("output.png")
files.download("watermarked_image.png")
