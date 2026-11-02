
import cv2
from google.colab import files

# Upload input video
uploaded = files.upload()
filename = next(iter(uploaded))

# Function to play video in reverse slow motion
def reverse_slow_motion(input_video, output_video):

    cap = cv2.VideoCapture(input_video)

    if not cap.isOpened():
        raise ValueError("Video could not be opened.")

    fps = cap.get(cv2.CAP_PROP_FPS)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Read all video frames
    frames = []

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        frames.append(frame)

    cap.release()

    if not frames:
        raise ValueError("No frames found in video.")

    # Reverse the frame order
    frames.reverse()

    # Reduce frame rate for slow motion
    slow_fps = max(fps / 2, 1)

    # Create output video
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(
        output_video, fourcc, slow_fps, (width, height)
    )

    # Write reversed frames
    for frame in frames:
        out.write(frame)

    out.release()

    print("Reverse slow-motion video created successfully.")

# Call the function
reverse_slow_motion(filename, "reverse_slow_motion.mp4")

# Download output video
files.download("reverse_slow_motion.mp4")

