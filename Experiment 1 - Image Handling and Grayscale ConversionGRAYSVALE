
import cv2
import matplotlib.pyplot as plt

# Read the input image
image = cv2.imread("input.jpg")

if image is None:
    print("Error: Image not found. Please add input.jpg.")
else:
    # Convert the image from BGR to RGB
    original = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Save the grayscale image
    cv2.imwrite("grayscale_image.jpg", gray)

    # Display both images
    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.imshow(original)
    plt.title("Original Image")
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.imshow(gray, cmap="gray")
    plt.title("Grayscale Image")
    plt.axis("off")

    plt.tight_layout()
    plt.savefig("output.png")
    plt.show()

    print("Image converted to grayscale successfully!")
