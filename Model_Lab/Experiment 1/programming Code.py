import cv2
img = cv2.imread('input.jpg')
if img is None:
    print("Image not found! Put input.jpg in same folder")
    exit()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
k = int(input("Kernel (odd): "))
blur = cv2.GaussianBlur(gray, (k, k), 0)

print("Done! Saving blurred.jpg")
cv2.imwrite('blurred.jpg', blur)

cv2.imshow('Original', gray)
cv2.imshow('Blurred', blur)
print("Windows opened - check taskbar, press any key to close")
cv2.waitKey(0)
cv2.destroyAllWindows()
