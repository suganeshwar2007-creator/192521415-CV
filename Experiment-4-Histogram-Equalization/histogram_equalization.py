
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
    # Step 3: Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Step 4: Apply histogram equalization
    equalized = cv2.equalizeHist(gray)

    # Step 5: Display original and equalized images
    original_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    plt.figure(figsize=(12, 8))

    plt.subplot(2, 2, 1)
    plt.imshow(original_rgb)
    plt.title("Original Image")
    plt.axis("off")

    plt.subplot(2, 2, 2)
    plt.imshow(equalized, cmap="gray")
    plt.title("Histogram Equalized Image")
    plt.axis("off")

    # Step 6: Compare histograms
    plt.subplot(2, 2, 3)
    plt.hist(gray.ravel(), 256, [0, 256])
    plt.title("Original Histogram")
    plt.xlabel("Pixel Intensity")
    plt.ylabel("Frequency")

    plt.subplot(2, 2, 4)
    plt.hist(equalized.ravel(), 256, [0, 256])
    plt.title("Equalized Histogram")
    plt.xlabel("Pixel Intensity")
    plt.ylabel("Frequency")

    plt.tight_layout()

    # Step 7: Save the output
    plt.savefig("output.png", bbox_inches="tight")
    cv2.imwrite("equalized_image.png", equalized)

    plt.show()

    print("Histogram equalization completed successfully!")

    # Step 8: Download the output files
    files.download("output.png")
    files.download("equalized_image.png")
