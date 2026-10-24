
import cv2
import matplotlib.pyplot as plt
from google.colab import files

uploaded = files.upload()
img = cv2.imread(next(iter(uploaded)), 0)

sobel_x = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)

sobel = cv2.addWeighted(
    cv2.convertScaleAbs(sobel_x), 0.5,
    cv2.convertScaleAbs(sobel_y), 0.5, 0
)

plt.subplot(1, 2, 1)
plt.imshow(img, cmap='gray')
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(sobel, cmap='gray')
plt.title("Sobel Filtered Image")
plt.axis("off")

plt.tight_layout()
plt.savefig("output.png")
plt.show()

cv2.imwrite("sobel_filtered.png", sobel)
files.download("output.png")
files.download("sobel_filtered.png")
