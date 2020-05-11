from PIL import Image
from skimage import data,filters
import cv2
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.image as mpimg

#im = Image.open("1.jpg")
#pts1=np.float32([[0,0],[50,0],[154,154],[0,154]])
#pts2=np.float32([[0,0],[50,0],[154,154],[0,154]])
img = cv2.imread('3.jpeg')
#mat=cv2.getPerspectiveTransform(pts1,pts2)
#imgout=cv2.warpPerspective(img,mat,(154,154))
#canimg=cv2.Canny(img,100,100)
#cv2.imshow("can",canimg)
#image=mpimg.imread("1.jpg")
#plt.imshow(image)
#plt.show()
imggray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgblur=cv2.GaussianBlur(imggray,(7,7),1)
cv2.imshow("imgout",img)
cv2.imshow("blur",imgblur)
cv2.waitKey(0)
