
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

    # Step 4: Detect edges using the Canny function
    edges = cv2.Canny(gray, 100, 200)

    # Step 5: Display original and outline images
    original_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.imshow(original_rgb)
    plt.title("Original Image")
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.imshow(edges, cmap="gray")
    plt.title("Canny Edge Detection")
    plt.axis("off")

    plt.tight_layout()

    # Step 6: Save output images
    plt.savefig("output.png", bbox_inches="tight")
    cv2.imwrite("canny_edges.png", edges)

    plt.show()

    print("Canny edge detection completed successfully!")

    # Step 7: Download the output files
    files.download("output.png")
    files.download("canny_edges.png")
