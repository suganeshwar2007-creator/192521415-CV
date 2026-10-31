
import cv2
from google.colab import files
from IPython.display import Video, display

# Function to reverse a video
def reverse_video(input_path, output_path):

    # Open the input video
    cap = cv2.VideoCapture(input_path)

    if not cap.isOpened():
        raise ValueError("Error: Unable to open the video.")

    # Get video properties
    fps = cap.get(cv2.CAP_PROP_FPS)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    if fps <= 0:
        fps = 25

    # Store all video frames
    frames = []

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        frames.append(frame)

    cap.release()

    if len(frames) == 0:
        raise ValueError("Error: No frames found in the video.")

    print("Total frames:", len(frames))

    # Create output video
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    writer = cv2.VideoWriter(
        output_path, fourcc, fps, (width, height)
    )

    if not writer.isOpened():
        raise ValueError("Error: Unable to create output video.")

    # Write frames in reverse order
    for frame in reversed(frames):
        writer.write(frame)

    writer.release()

    print("Reverse video created successfully!")

# Upload input video
uploaded = files.upload()
input_video = next(iter(uploaded))

# Reverse the video
output_video = "reverse_video.mp4"
reverse_video(input_video, output_video)

# Display the reversed video
display(Video(output_video, embed=True))

# Download the output video
files.download(output_video)
