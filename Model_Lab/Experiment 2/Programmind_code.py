import cv2
img = cv2.imread('input.jpg')
if img is None:
    print("Image not found! Put input.jpg in same folder")
    exit()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
T = int(input("Threshold: "))
_, binary = cv2.threshold(gray, T, 255, cv2.THRESH_BINARY)

print("Done! Saving binary.jpg")
cv2.imwrite('binary.jpg', binary)

cv2.imshow('Original', gray)
cv2.imshow('Binary', binary)
print("Windows opened - check taskbar, press any key to close")
cv2.waitKey(0)
cv2.destroyAllWindows()
