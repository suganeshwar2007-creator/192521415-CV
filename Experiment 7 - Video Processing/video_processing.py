
import cv2
from google.colab import files
from IPython.display import Video, display

# Upload a captured video
uploaded = files.upload()
filename = next(iter(uploaded))

# Read the video
cap = cv2.VideoCapture(filename)

if not cap.isOpened():
    raise ValueError("Error: Unable to open the video.")

# Get video properties
fps = cap.get(cv2.CAP_PROP_FPS)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

if fps <= 0 or width <= 0 or height <= 0:
    cap.release()
    raise ValueError("Invalid video properties.")

print("Original FPS:", fps)
print("Video resolution:", width, "x", height)

# Create output video writers
fourcc = cv2.VideoWriter_fourcc(*"mp4v")

slow_writer = cv2.VideoWriter(
    "slow_motion.mp4", fourcc, max(fps / 2, 1), (width, height)
)

fast_writer = cv2.VideoWriter(
    "fast_motion.mp4", fourcc, fps, (width, height)
)

frame_number = 0

# Process the captured video
while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Slow motion: keep every frame, play at half the FPS
    slow_writer.write(frame)

    # Fast motion: keep every second frame
    if frame_number % 2 == 0:
        fast_writer.write(frame)

    frame_number += 1

cap.release()
slow_writer.release()
fast_writer.release()

print("Slow-motion and fast-motion videos created successfully.")

# Display slow-motion video
print("Slow Motion Video")
display(Video("slow_motion.mp4", embed=True))

# Display fast-motion video
print("Fast Motion Video")
display(Video("fast_motion.mp4", embed=True))

# Download output videos
files.download("slow_motion.mp4")
files.download("fast_motion.mp4")
