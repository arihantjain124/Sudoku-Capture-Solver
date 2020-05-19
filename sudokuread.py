import cv2
import numpy as np
from sudokucapture import sudokucap
import time
from numpy import loadtxt
import keras
from keras import backend as K
from keras.layers.core import Dense, Activation
from keras.optimizers import Adam
from keras.metrics import categorical_crossentropy
from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing import image
from keras.models import Model
from keras.applications import imagenet_utils
from keras.layers import Dense, GlobalAveragePooling2D
from keras.applications import MobileNet
from keras.applications.mobilenet import preprocess_input
import numpy as np
from IPython.display import Image
from keras.optimizers import Adam
from keras.callbacks import ModelCheckpoint, LearningRateScheduler, TensorBoard, EarlyStopping
from keras.layers import Dropout, Flatten
import tensorflow as tf
gpus = tf.config.experimental.list_physical_devices('GPU')
tf.config.experimental.set_memory_growth(gpus[0], True)
model = tf.keras.models.load_model("weights3.h5")
model._make_predict_function()
img = cv2.imread("3.jpeg")

digits=['0','1','2','3','4','5','6','7','8','9']
# imggray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# imgblur=cv2.GaussianBlur(imggray,(7,7),0.5)
# imgcanny=cv2.Canny((imgblur),80,80)
# cv2.imshow("asd",imgcanny)
flag, img = sudokucap(img)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
for i in range(0, 530, 66):
    for j in range(0, 530, 66):
        num = img[i:i+66, j:j+66]
        m = num[np.newaxis, ...]
        m= tf.cast(m,tf.float32)
        a=model.predict(m)
        print(digits[np.argmax(a)])
        cv2.imshow("a",num)
        time.sleep(3)
        cv2.waitKey(1)
        
# scale_percent = 60 # percent of original size
# width = int(img.shape[1] * scale_percent / 100)
# height = int(img.shape[0] * scale_percent / 100)
# dim = (width, height)
# img =cv2.resize(img,dim)
# imgblur=cv2.GaussianBlur(img,(11,11),1)
# imgcanny=cv2.Canny(imgblur,50,50)
# imgbg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# edges = cv2.Canny(imgbg,50,150,apertureSize = 3)
# lines = cv2.HoughLines(edges,1,np.pi/180,200)
# for l in lines:
#     rho,theta=l[0]
#     a = np.cos(theta)
#     b = np.sin(theta)
#     x0 = a*rho
#     y0 = b*rho
#     x1 = int(x0 + 1000*(-b))
#     y1 = int(y0 + 1000*(a))
#     x2 = int(x0 - 1000*(-b))
#     y2 = int(y0 - 1000*(a))
#     cv2.line(img,(x1,y1),(x2,y2),(0,0,255),1)
# cv2.imwrite('houghlines3.jpg',img)
