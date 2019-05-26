import cv2

for i in range(1, 7435):
    img = cv2.imread("neg/" + str(i) + ".jpg", cv2.IMREAD_GRAYSCALE)
    re = cv2.resize(img, (100, 100))
    cv2.imwrite("neg_1/" + str(i) + ".jpg", re)
