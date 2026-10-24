# Experiment 17 - Image Watermarking Using OpenCV

## Aim
To design and implement a watermarking technique to insert a watermark into an original image using OpenCV.

## Libraries Used
- Python
- OpenCV
- Matplotlib

## Method
1. Read the original image using OpenCV.
2. Create a copy of the original image.
3. Add watermark text using `cv2.putText()`.
4. Blend the watermark overlay with the original image using `cv2.addWeighted()`.
5. Display the original and watermarked images.
6. Save the output images.

## Output

![Image Watermarking Output](output.png)

## Result
The watermark was successfully inserted into the original image using Python and OpenCV.
