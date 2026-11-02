
import cv2
import matplotlib.pyplot as plt
from google.colab import files

# Function to add text to an image
def add_text(image, text):

    # Copy the original image
    output = image.copy()

    # Add text to the image
    cv2.putText(
        output,
        text,
        (50, 100),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 0, 255),
        2,
        cv2.LINE_AA
    )

    return output


# Step 1: Upload an image
uploaded = files.upload()
filename = next(iter(uploaded))

# Step 2: Read the image
image = cv2.imread(filename)

if image is None:
    raise ValueError("Error: Unable to read the image.")

# Step 3: Get text from the user
user_text = input("Enter the text to display on the image: ")

if not user_text.strip():
    raise ValueError("Please enter some text.")

# Step 4: Add text to the image
result = add_text(image, user_text)

# Step 5: Save the output image
cv2.imwrite("text_output.png", result)

# Step 6: Display original and output images
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(result, cv2.COLOR_BGR2RGB))
plt.title("Image with Text")
plt.axis("off")

plt.tight_layout()
plt.savefig("output.png")
plt.show()

print("Text added successfully!")

# Step 7: Download output images
files.download("text_output.png")
files.download("output.png")
