# Experiment 15 - Harris Corner Detection Using OpenCV

## Aim
To read an image in Python and detect corners using the Harris Corner Detection function.

## Libraries Used
- Python
- OpenCV
- NumPy
- Matplotlib

## Method
1. Read the input image using OpenCV.
2. Convert the image to grayscale.
3. Convert the grayscale image to `float32`.
4. Apply Harris Corner Detection using `cv2.cornerHarris()`.
5. Dilate the corner responses to improve visibility.
6. Highlight detected corners in red.
7. Display and save the output images.

## Output

![Harris Corner Detection Output](output.png)

## Result
Corners in the input image were successfully detected using the Harris Corner Detection function in OpenCV.
