from sudokucapture import sudokucap
import cv2

img = cv2.imread("Test_Images/21.jpeg")
flag, img = sudokucap(img)
cv2.imshow("cap", img)
cv2.waitKey(0)
