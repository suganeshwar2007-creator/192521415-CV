# Experiment 39 - Reverse Slow Motion Video Using OpenCV

## Aim
To write a Python function to play a given video in reverse mode in slow motion using OpenCV.

## Software Requirements
- Python
- OpenCV
- Google Colab

## Algorithm
1. Import the required libraries.
2. Upload the input video.
3. Open the video using `cv2.VideoCapture()`.
4. Read the video frames one by one.
5. Store all frames in a list.
6. Reverse the order of the frames using `frames.reverse()`.
7. Reduce the original frame rate to half for slow-motion playback.
8. Create an output video using `cv2.VideoWriter()`.
9. Write the reversed frames into the output video.
10. Save and download the output video.

## Python Functions Used
- `cv2.VideoCapture()` – Opens the input video.
- `cap.read()` – Reads video frames.
- `frames.reverse()` – Reverses the order of frames.
- `cv2.VideoWriter()` – Creates the output video.
- `cv2.VideoWriter_fourcc()` – Specifies the video codec.
- `out.write()` – Writes frames into the output video.
- `cap.release()` – Releases the input video.
- `out.release()` – Saves and closes the output video.

## Input
A video file in MP4 format.

## Output
The output video plays the original video in reverse direction at half the original frame rate.

**Output File:** `reverse_slow_motion.mp4`

## Result
Thus, the given video was successfully played in reverse mode in slow motion using the OpenCV library.

## Note
The program stores video frames in memory before reversing them. Therefore, short video files are recommended for this experiment.
