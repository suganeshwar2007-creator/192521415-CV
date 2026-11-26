import cv2
img = cv2.imread(r'C:\Users\Sugan\PyCharmMiscProject\input.jpg')
out = img.copy()
cv2.putText(out, "SIMATS - Suganeshwar K", (20, img.shape[0]-20),
            cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
cv2.imshow('Watermarked', out)
cv2.imwrite('watermarked.jpg', out)
cv2.waitKey(0)
cv2.destroyAllWindows()
