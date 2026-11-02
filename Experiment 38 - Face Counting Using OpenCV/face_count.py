
import cv2
import matplotlib.pyplot as plt
from google.colab import files

# Upload input image
uploaded = files.upload()
filename = next(iter(uploaded))

# Read image
img = cv2.imread(filename)

if img is None:
    raise ValueError("Image could not be loaded.")

# Function to count faces
def count_faces(image):

    # Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Load Haar Cascade face detector
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades +
        "haarcascade_frontalface_default.xml"
    )

    # Detect faces
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )

    # Draw rectangles around detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(
            image, (x, y), (x + w, y + h),
            (0, 255, 0), 2
        )

    # Count total faces
    total_faces = len(faces)

    # Display face count
    cv2.putText(
        image,
        "Number of Faces: " + str(total_faces),
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 0, 255),
        2
    )

    return image, total_faces

# Call the function
output, total = count_faces(img.copy())

print("Total number of faces detected:", total)

# Display output
plt.figure(figsize=(10, 6))
plt.imshow(cv2.cvtColor(output, cv2.COLOR_BGR2RGB))
plt.title("Face Detection and Counting")
plt.axis("off")
plt.show()

# Save output image
cv2.imwrite("face_count_output.png", output)

# Download output
files.download("face_count_output.png")
