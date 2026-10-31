
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

# Step 4: Load Haar Cascade face detector
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades +
    "haarcascade_frontalface_default.xml"
)

# Step 5: Load Haar Cascade smile detector
smile_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades +
    "haarcascade_smile.xml"
)

if face_cascade.empty() or smile_cascade.empty():
    raise ValueError("Error: Haar Cascade model not loaded.")

# Step 6: Detect faces
faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(50, 50)
)

# Step 7: Detect smiles inside each face
output = image.copy()
smile_count = 0

for (x, y, w, h) in faces:

    # Extract face region
    face_gray = gray[y:y+h, x:x+w]

    # Search in lower part of face
    mouth_region = face_gray[h//2:h, :]

    smiles = smile_cascade.detectMultiScale(
        mouth_region,
        scaleFactor=1.7,
        minNeighbors=20,
        minSize=(25, 15)
    )

    # Draw rectangles around detected smiles
    for (sx, sy, sw, sh) in smiles:

        cv2.rectangle(
            output,
            (x + sx, y + h//2 + sy),
            (x + sx + sw, y + h//2 + sy + sh),
            (0, 255, 0),
            2
        )

        cv2.putText(
            output,
            "Smile",
            (x + sx, y + h//2 + sy - 5),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (0, 255, 0),
            2
        )

        smile_count += 1

# Step 8: Display result
print("Number of faces detected:", len(faces))
print("Number of smiles detected:", smile_count)

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(output, cv2.COLOR_BGR2RGB))
plt.title("Smile Detection")
plt.axis("off")

plt.tight_layout()
plt.savefig("output.png")
plt.show()

# Step 9: Save and download output
cv2.imwrite("smile_detected.png", output)

files.download("output.png")
files.download("smile_detected.png")
