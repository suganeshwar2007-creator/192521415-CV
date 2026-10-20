
import cv2
import matplotlib.pyplot as plt
from google.colab import files

# Function to analyze the color histogram
def analyze_histogram(image):
    colors = ('b', 'g', 'r')
    channel_names = ('Blue', 'Green', 'Red')

    plt.figure(figsize=(10, 5))

    for i, (color, name) in enumerate(zip(colors, channel_names)):
        histogram = cv2.calcHist(
            [image], [i], None, [256], [0, 256]
        )

        plt.plot(histogram, color=color, label=name)

    plt.title("Color Histogram Analysis")
    plt.xlabel("Pixel Intensity (0-255)")
    plt.ylabel("Number of Pixels")
    plt.xlim([0, 256])
    plt.legend()
    plt.grid(True, alpha=0.3)


# Upload an image
uploaded = files.upload()
filename = next(iter(uploaded))

# Read the image
image = cv2.imread(filename)

if image is None:
    print("Error: Unable to read the image.")
else:
    # Convert BGR to RGB for display
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Display the input image
    plt.figure(figsize=(6, 4))
    plt.imshow(image_rgb)
    plt.title("Input Image")
    plt.axis("off")
    plt.show()

    # Analyze and save the color histogram
    analyze_histogram(image)
    plt.tight_layout()
    plt.savefig("output.png", bbox_inches="tight")
    plt.show()

    print("Color histogram analysis completed successfully!")

    # Download the histogram output
    files.download("output.png")
