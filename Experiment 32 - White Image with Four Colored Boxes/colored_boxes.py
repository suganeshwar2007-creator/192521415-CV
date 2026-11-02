
import cv2
import numpy as np
import matplotlib.pyplot as plt
from google.colab import files

# Function to create a white image with four colored boxes
def create_colored_boxes(width, height):

    # Create a white image
    image = np.ones((height, width, 3), dtype=np.uint8) * 255

    # Calculate box size (1/10th of image size)
    box_width = width // 10
    box_height = height // 10

    # Top-left corner - Black
    image[0:box_height, 0:box_width] = [0, 0, 0]

    # Top-right corner - Blue
    image[0:box_height, width-box_width:width] = [255, 0, 0]

    # Bottom-left corner - Green
    image[height-box_height:height, 0:box_width] = [0, 255, 0]

    # Bottom-right corner - Red
    image[height-box_height:height, width-box_width:width] = [0, 0, 255]

    return image


# Get image size from user
width = int(input("Enter image width: "))
height = int(input("Enter image height: "))

# Validate image dimensions
if width < 10 or height < 10:
    raise ValueError("Width and height must be at least 10 pixels.")

# Create the image
result = create_colored_boxes(width, height)

# Save the image
cv2.imwrite("colored_boxes.png", result)

# Display the image
plt.figure(figsize=(8, 6))
plt.imshow(cv2.cvtColor(result, cv2.COLOR_BGR2RGB))
plt.title("White Image with Four Colored Boxes")
plt.axis("off")
plt.show()

print("Image created successfully!")

# Download the image
files.download("colored_boxes.png")
