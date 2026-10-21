# Experiment 8 - Image Dilation Using OpenCV

## Aim
To read an image in Python and perform image dilation using the OpenCV Dilate function.

## Libraries Used
- Python
- OpenCV
- NumPy
- Matplotlib

## Method
1. Read the input image using OpenCV.
2. Convert the image into grayscale.
3. Create a 5 × 5 kernel using NumPy.
4. Apply dilation using `cv2.dilate()`.
5. Display the original and dilated images.
6. Save the output images.

## Output

![Image Dilation Output](output.png)

## Result
The input image was successfully read and processed using the OpenCV dilation function. The bright foreground regions expanded after dilation.
