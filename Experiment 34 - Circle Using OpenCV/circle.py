
import cv2
import numpy as np
import matplotlib.pyplot as plt
from google.colab import files

# Function to create a white image and draw a circle
def create_circle(width, height):

    # Create a white image
    image = np.ones((height, width, 3), dtype=np.uint8) * 255

    # Calculate circle center and radius
    center_x = width // 2
    center_y = height // 2
    radius = min(width, height) // 4

    # Draw circle
    cv2.circle(
        image,
        (center_x, center_y),
        radius,
        (0, 0, 255),
        3
    )

    return image


# Get image size from user
width = int(input("Enter image width: "))
height = int(input("Enter image height: "))

# Validate dimensions
if width <= 0 or height <= 0:
    raise ValueError("Image width and height must be positive.")

# Create circle image
result = create_circle(width, height)

# Save image
cv2.imwrite("circle.png", result)

# Display image
plt.figure(figsize=(8, 6))
plt.imshow(cv2.cvtColor(result, cv2.COLOR_BGR2RGB))
plt.title("Circle on White Image")
plt.axis("off")
plt.show()

print("Circle created successfully!")

# Download output
files.download("circle.png")
