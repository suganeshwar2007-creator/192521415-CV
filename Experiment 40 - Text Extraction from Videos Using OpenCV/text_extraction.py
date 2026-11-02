
# Install required libraries
!apt-get install -y tesseract-ocr
!pip install -q pytesseract opencv-python-headless

import cv2
import pytesseract
from google.colab import files

# Upload video
uploaded = files.upload()
filename = next(iter(uploaded))

# Function to extract text from video
def extract_text_from_video(video_path):

    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        raise ValueError("Video could not be opened.")

    extracted_text = []
    frame_number = 0

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        frame_number += 1

        # Process every 30th frame
        if frame_number % 30 == 0:

            # Convert frame to grayscale
            gray = cv2.cvtColor(
                frame, cv2.COLOR_BGR2GRAY
            )

            # Extract text using OCR
            text = pytesseract.image_to_string(gray)

            if text.strip():
                extracted_text.append(
                    f"Frame {frame_number}:\n{text.strip()}"
                )

    cap.release()

    return extracted_text

# Call the function
result = extract_text_from_video(filename)

# Display extracted text
if result:
    print("Extracted Text:\n")

    for text in result:
        print(text)
        print("--------------------")
else:
    print("No text detected in the video.")

# Save extracted text
with open("extracted_text.txt", "w", encoding="utf-8") as file:
    file.write("\n\n".join(result))

# Download text file
files.download("extracted_text.txt")
