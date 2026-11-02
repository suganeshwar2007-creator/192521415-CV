# Experiment 36 - Background Subtraction Based on Color Levels Using OpenCV

## Aim
To write a Python function to subtract the background from a given input image based on color levels using OpenCV.

## Software Requirements
- Python
- OpenCV
- NumPy
- Matplotlib
- Google Colab

## Algorithm
1. Import the required libraries.
2. Upload and read the input image.
3. Convert the image from BGR color space to HSV color space.
4. Define the lower and upper color levels of the background.
5. Use `cv2.inRange()` to identify the background color.
6. Invert the mask to select the foreground.
7. Use `cv2.bitwise_and()` to remove the background.
8. Display the original and background-removed images.
9. Save the output image.

## Python Functions Used
- `cv2.imread()` – Reads the input image.
- `cv2.cvtColor()` – Converts BGR to HSV color space.
- `cv2.inRange()` – Detects pixels within the specified color range.
- `cv2.bitwise_not()` – Inverts the mask.
- `cv2.bitwise_and()` – Removes the selected background.
- `cv2.imwrite()` – Saves the output image.

## Input
An image containing a colored background.

## Output
The output image displays the foreground object with the selected background color removed.

**Output File:** `background_removed.png`

## Result
Thus, the background was successfully subtracted from the given input image based on color levels using the OpenCV library.

## Note
The program uses a green color range as an example. The lower and upper HSV values can be changed according to the background color of the input image.
