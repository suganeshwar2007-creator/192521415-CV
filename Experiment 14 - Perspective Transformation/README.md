# Experiment 14 - Perspective Transformation Using OpenCV

## Aim
To perform perspective transformation on an input image using Python and OpenCV.

## Libraries Used
- Python
- OpenCV
- NumPy
- Matplotlib

## Method
1. Read the input image using OpenCV.
2. Define four source points and four destination points.
3. Calculate the perspective transformation matrix using `cv2.getPerspectiveTransform()`.
4. Apply the transformation using `cv2.warpPerspective()`.
5. Display the original and transformed images.
6. Save the output images.

## Output

![Perspective Transformation Output](output.png)

## Result
Perspective transformation was successfully applied to the input image using Python and OpenCV.
