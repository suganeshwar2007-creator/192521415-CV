
import cv2
import numpy as np
import matplotlib.pyplot as plt
from google.colab import files

# Function to create a white image and draw a rectangle
def create_rectangle(width, height):

    # Create a white image
    image = np.ones((height, width, 3), dtype=np.uint8) * 255

    # Calculate rectangle coordinates
    x1 = width // 4
    y1 = height // 4
    x2 = 3 * width // 4
    y2 = 3 * height // 4

    # Draw rectangle
    cv2.rectangle(
        image,
        (x1, y1),
        (x2, y2),
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

# Create rectangle image
result = create_rectangle(width, height)

# Save image
cv2.imwrite("rectangle.png", result)

# Display image
plt.figure(figsize=(8, 6))
plt.imshow(cv2.cvtColor(result, cv2.COLOR_BGR2RGB))
plt.title("Rectangle on White Image")
plt.axis("off")
plt.show()

print("Rectangle created successfully!")

# Download output
files.download("rectangle.png")
