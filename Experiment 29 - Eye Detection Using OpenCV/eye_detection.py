
import cv2
import matplotlib.pyplot as plt
from google.colab import files

# Step 1: Upload an image
uploaded = files.upload()
filename = next(iter(uploaded))

# Step 2: Read the image
image = cv2.imread(filename)

if image is None:
    raise ValueError("Error: Unable to read the image.")

# Step 3: Convert image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Step 4: Load Haar Cascade eye detector
eye_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades +
    "haarcascade_eye.xml"
)

if eye_cascade.empty():
    raise ValueError("Error: Eye detection model not loaded.")

# Step 5: Detect eyes
eyes = eye_cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=8,
    minSize=(20, 20)
)

# Step 6: Draw rectangles around detected eyes
output = image.copy()

for (x, y, w, h) in eyes:
    cv2.rectangle(
        output,
        (x, y),
        (x + w, y + h),
        (0, 255, 0),
        2
    )

    cv2.putText(
        output,
        "Eye",
        (x, y - 5),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.5,
        (0, 255, 0),
        2
    )

# Step 7: Display number of detected eyes
print("Number of eyes detected:", len(eyes))

# Step 8: Display original and detected images
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(output, cv2.COLOR_BGR2RGB))
plt.title("Eye Detection")
plt.axis("off")

plt.tight_layout()
plt.savefig("output.png")
plt.show()

# Step 9: Save and download output
cv2.imwrite("eye_detected.png", output)

files.download("output.png")
files.download("eye_detected.png")
