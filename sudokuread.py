import cv2
import numpy as np
from sudokucapture import sudokucap
import time
from numpy import loadtxt
import numpy as np
import pickle
import tensorflow as tf

physical_devices = tf.config.experimental.list_physical_devices('GPU')
tf.config.experimental.set_memory_growth(physical_devices[0], True)


def preProcessing(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.equalizeHist(img)
    img = img / 255
    return img


pickle_in = open("digitread.p", "rb")
model = pickle.load(pickle_in)
img = cv2.imread("Test_Images/2.png")
flag, img = sudokucap(img)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
puz = []
temp = []
for i in range(0, 530, 66):
    for j in range(0, 530, 66):
        cell = img[i:i + 66, j:j + 66]
        cell = cv2.resize(cell, (32, 32))
        cell = preProcessing(cell)
        pre = cell.reshape(1, 32, 32, 1)
        digit = int(model.predict_classes(pre))
        # print(digit)
        temp.append(digit)
        # cv2.imshow("a", cell)
        # time.sleep(1)
        cv2.waitKey(1)
    puz.append(temp)
    temp = []
print(puz)
