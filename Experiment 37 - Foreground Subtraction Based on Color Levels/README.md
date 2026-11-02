# Experiment 37 - Foreground Subtraction Based on Color Levels Using OpenCV

## Aim
To write a Python function to subtract the foreground from a given input image based on color levels using OpenCV.

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
4. Define the lower and upper color levels of the foreground.
5. Use `cv2.inRange()` to identify the foreground color.
6. Invert the mask to select the background.
7. Use `cv2.bitwise_and()` to remove the foreground.
8. Display the original and foreground-removed images.
9. Save the output image.

## Python Functions Used
- `cv2.imread()` – Reads the input image.
- `cv2.cvtColor()` – Converts BGR to HSV color space.
- `cv2.inRange()` – Detects pixels within the specified color range.
- `cv2.bitwise_not()` – Inverts the mask.
- `cv2.bitwise_and()` – Removes the selected foreground.
- `cv2.imwrite()` – Saves the output image.

## Input
An image containing a foreground object with a distinguishable color.

## Output
The output image displays the remaining background after removing the selected foreground color.

**Output File:** `foreground_removed.png`

## Result
Thus, the foreground was successfully subtracted from the given input image based on color levels using the OpenCV library.

## Note
The program uses a red color range as an example. The lower and upper HSV values can be changed according to the foreground color of the input image.
