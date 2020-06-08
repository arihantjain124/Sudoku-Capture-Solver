import cv2
import numpy as np


def reorder(coor):
    coor = coor.reshape(4, 2)
    coornew = np.zeros((4, 1, 2), np.int32)
    add = coor.sum(1)
    coornew[0] = coor[np.argmin(add)]
    coornew[3] = coor[np.argmax(add)]
    diff = np.diff(coor, axis=1)
    coornew[1] = coor[np.argmin(diff)]
    coornew[2] = coor[np.argmax(diff)]
    return coornew


def getWrap(img, coor, dim):
    pts1 = np.float32(reorder(coor))
    pts2 = np.float32([[0, 0], [dim[0], 0], [0, dim[1]], [dim[0], dim[1]]])
    mat = cv2.getPerspectiveTransform(pts1, pts2)
    imgwrap = cv2.warpPerspective(img, mat, (dim[0], dim[1]))
    return imgwrap


def preprocess(img):
    imggray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgblur = cv2.GaussianBlur(imggray, (5, 5), 0.5)
    imgcanny = cv2.Canny((imgblur), 80, 80)
    kernel = np.ones((5, 5))
    imgdial = cv2.dilate(imgcanny, kernel, iterations=1)
    final = cv2.erode(imgdial, kernel, iterations=1)
    return imgcanny


def getcontour(img):
    found = False
    maxArea = 0
    biggest = np.zeros((4, 1, 2))
    contours, hierarchy = cv2.findContours(
        img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area >= 5000:
            # cv2.drawContours(imgcon,cnt,-1,(255,0,0),3)
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02*peri, True)
            if area > maxArea and len(approx) == 4:
                biggest = approx
                maxArea = area
                found = True
    return found, biggest


def sudokucap(img):
    scale_percent = 60  # percent of original size
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    img = cv2.resize(img, dim)
    imgthre = preprocess(img)
    success, sudokucoor = getcontour(imgthre)
    if success == True:
        sudokufinal = getWrap(img, sudokucoor, dim)
        sudokufinal = cv2.resize(sudokufinal, (600, 600))
        return success, sudokufinal
    else:
        sudokufinal = cv2.resize(img, (600, 600))
        return success, sudokufinal
