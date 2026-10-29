
import cv2
import torch
import matplotlib.pyplot as plt
from google.colab import files
from PIL import Image
from transformers import OwlViTProcessor, OwlViTForObjectDetection

# Upload the input image
uploaded = files.upload()
filename = next(iter(uploaded))

# Read image using OpenCV
image = cv2.imread(filename)

if image is None:
    raise ValueError("Unable to read the image.")

# Load pre-trained object detection model
model_name = "google/owlvit-base-patch32"
processor = OwlViTProcessor.from_pretrained(model_name)
model = OwlViTForObjectDetection.from_pretrained(model_name)

# Convert image to RGB
rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
pil_image = Image.fromarray(rgb_image)

# Detect a watch
inputs = processor(
    text=[["a wristwatch", "a watch"]],
    images=pil_image,
    return_tensors="pt"
)

with torch.no_grad():
    outputs = model(**inputs)

# Get detected objects and bounding boxes
target_sizes = torch.tensor([pil_image.size[::-1]])
results = processor.post_process_object_detection(
    outputs=outputs,
    target_sizes=target_sizes,
    threshold=0.1
)[0]

# Draw bounding boxes
count = 0

for score, box in zip(results["scores"], results["boxes"]):
    x1, y1, x2, y2 = map(int, box.tolist())

    cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
    label = f"Watch: {score.item():.2f}"
    cv2.putText(
        image, label, (x1, max(y1 - 10, 20)),
        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2
    )
    count += 1

# Display the result
result_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

plt.figure(figsize=(10, 6))
plt.imshow(result_image)
plt.title("Watch Recognition")
plt.axis("off")
plt.tight_layout()
plt.savefig("output.png")
plt.show()

if count == 0:
    print("No watch detected. Try another image.")

cv2.imwrite("watch_recognized.png", image)
files.download("output.png")
files.download("watch_recognized.png")
