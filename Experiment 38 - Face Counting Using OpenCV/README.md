# Experiment 38 - Face Counting Using OpenCV

## Aim
To write a Python function to count the number of faces in a given input image using OpenCV.

## Software Requirements
- Python
- OpenCV
- Matplotlib
- Google Colab

## Algorithm
1. Import the required libraries.
2. Upload and read the input image.
3. Convert the image into grayscale.
4. Load the Haar Cascade face detection classifier.
5. Use `detectMultiScale()` to detect faces in the image.
6. Draw rectangles around the detected faces.
7. Count the total number of detected faces using `len()`.
8. Display the total face count on the image.
9. Display and save the output image.

## Python Functions Used
- `cv2.imread()` – Reads the input image.
- `cv2.cvtColor()` – Converts the image into grayscale.
- `cv2.CascadeClassifier()` – Loads the Haar Cascade classifier.
- `detectMultiScale()` – Detects faces in the image.
- `cv2.rectangle()` – Draws rectangles around detected faces.
- `len()` – Counts the number of detected faces.
- `cv2.putText()` – Displays the face count.
- `cv2.imwrite()` – Saves the output image.

## Input
An image containing one or more human faces.

## Output
The output image displays green rectangles around the detected faces and shows the total number of faces.

**Output File:** `face_count_output.png`

## Result
Thus, the number of faces in the given input image was successfully detected and counted using the OpenCV library.

## Note
The Haar Cascade classifier works best with clear, front-facing faces. Detection accuracy may vary depending on image quality, face orientation, and lighting conditions.
