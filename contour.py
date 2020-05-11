import cv2
import numpy as np
from sudokucapture import sudokucap
img =cv2.imread("3.jpeg")
img=sudokucap(img)
# scale_percent = 60 # percent of original size
# width = int(img.shape[1] * scale_percent / 100)
# height = int(img.shape[0] * scale_percent / 100)
# dim = (width, height)
# img =cv2.resize(img,dim)
# # imgblur=cv2.GaussianBlur(img,(11,11),1)
# # imgcanny=cv2.Canny(imgblur,50,50)
imgbg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(imgbg,50,150,apertureSize = 3)
lines = cv2.HoughLines(edges,1,np.pi/180,200)
imgblank=np.zeros_like(img)
for l in lines:
    rho,theta=l[0]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    x1 = int(x0 + 1000*(-b))
    y1 = int(y0 + 1000*(a))
    x2 = int(x0 - 1000*(-b))
    y2 = int(y0 - 1000*(a))
    cv2.line(imgblank,(x1,y1),(x2,y2),(0,0,255),1)
    cv2.line(img,(x1,y1),(x2,y2),(0,0,255),1)
#cv2.imwrite('houghlines3.jpg',img)
cv2.imshow("blur",img)
cv2.waitKey(0)
