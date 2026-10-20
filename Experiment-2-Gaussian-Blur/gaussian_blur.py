
import cv2
import matplotlib.pyplot as plt
from google.colab import files

# Step 1: Upload an image
uploaded = files.upload()
filename = next(iter(uploaded))

# Step 2: Read the image
image = cv2.imread(filename)

if image is None:
    print("Error: Unable to read the image.")
else:
    # Step 3: Convert BGR to RGB for display
    original = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Step 4: Apply Gaussian Blur
    blurred = cv2.GaussianBlur(image, (15, 15), 0)
    blurred_rgb = cv2.cvtColor(blurred, cv2.COLOR_BGR2RGB)

    # Step 5: Display original and blurred images
    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.imshow(original)
    plt.title("Original Image")
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.imshow(blurred_rgb)
    plt.title("Gaussian Blurred Image")
    plt.axis("off")

    plt.tight_layout()

    # Step 6: Save the output for GitHub
    plt.savefig("output.png", bbox_inches="tight")
    cv2.imwrite("gaussian_blur.jpg", blurred)
    plt.show()

    print("Gaussian Blur applied successfully!")

    # Step 7: Download output files
    files.download("output.png")
    files.download("gaussian_blur.jpg")
