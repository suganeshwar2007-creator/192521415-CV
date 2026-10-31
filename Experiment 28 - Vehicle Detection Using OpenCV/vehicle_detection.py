
import cv2
from google.colab import files
from IPython.display import Video, display
from ultralytics import YOLO

# Step 1: Upload input video
uploaded = files.upload()
input_video = next(iter(uploaded))

# Step 2: Load pretrained YOLO model
model = YOLO("yolov8n.pt")

# Vehicle class IDs in the COCO dataset:
# 2 = Car, 3 = Motorcycle, 5 = Bus, 7 = Truck
vehicle_classes = [2, 3, 5, 7]

# Step 3: Open the video
cap = cv2.VideoCapture(input_video)

if not cap.isOpened():
    raise ValueError("Error: Unable to open the input video.")

# Step 4: Get video properties
fps = cap.get(cv2.CAP_PROP_FPS)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

if fps <= 0:
    fps = 25

# Step 5: Create output video
output_video = "vehicle_detection_output.mp4"

fourcc = cv2.VideoWriter_fourcc(*"mp4v")
writer = cv2.VideoWriter(
    output_video, fourcc, fps, (width, height)
)

if not writer.isOpened():
    cap.release()
    raise ValueError("Error: Unable to create output video.")

frame_count = 0
vehicle_count = 0

# Step 6: Detect vehicles in every frame
while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Detect vehicles using YOLO
    results = model.predict(
        frame,
        classes=vehicle_classes,
        conf=0.25,
        verbose=False
    )

    # Draw bounding boxes and labels
    output_frame = results[0].plot()

    # Count detected vehicles in this frame
    count = len(results[0].boxes)
    vehicle_count += count

    # Write processed frame
    writer.write(output_frame)

    frame_count += 1

    if frame_count % 30 == 0:
        print("Processed frames:", frame_count)

# Step 7: Release resources
cap.release()
writer.release()

print("Vehicle detection completed successfully!")
print("Total frames processed:", frame_count)
print("Total vehicle detections across frames:", vehicle_count)

# Step 8: Display output video
display(Video(output_video, embed=True))

# Step 9: Download output video
files.download(output_video)
