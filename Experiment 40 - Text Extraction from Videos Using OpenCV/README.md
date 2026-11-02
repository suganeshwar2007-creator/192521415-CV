# Experiment 40 - Text Extraction from Videos Using OpenCV

## Aim
To write a Python function to extract text from a given video using OpenCV and OCR (Optical Character Recognition).

## Software Requirements
- Python
- OpenCV
- Pytesseract
- Tesseract OCR
- Google Colab

## Algorithm
1. Import the required libraries.
2. Install Tesseract OCR and Pytesseract.
3. Upload the input video.
4. Open the video using `cv2.VideoCapture()`.
5. Read the video frames one by one.
6. Select every 30th frame for text extraction.
7. Convert the selected frames into grayscale.
8. Use `pytesseract.image_to_string()` to extract text from the frames.
9. Store the extracted text in a list.
10. Display and save the extracted text in a text file.

## Python Functions Used
- `cv2.VideoCapture()` – Opens the input video.
- `cap.read()` – Reads video frames.
- `cv2.cvtColor()` – Converts frames into grayscale.
- `pytesseract.image_to_string()` – Extracts text using OCR.
- `cap.release()` – Releases the video file.
- `open()` – Creates and writes the extracted text into a file.

## Input
A video file in MP4 format containing visible text.

## Output
The extracted text from the video frames is displayed and saved in a text file.

**Output File:** `extracted_text.txt`

## Result
Thus, text was successfully extracted from the given video using OpenCV and Tesseract OCR.

## Note
The program processes every 30th frame. Text extraction accuracy depends on video quality, text visibility, and frame selection. This experiment extracts visible text, not spoken audio.
