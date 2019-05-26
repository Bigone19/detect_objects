import cv2

img = cv2.imread("pos/" + str(12) + ".png", cv2.IMREAD_GRAYSCALE)
re = cv2.resize(img, (50, 50))
cv2.imwrite("resized/pos_12.png", re)
