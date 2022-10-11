import cv2
import math
import matplotlib
import numpy as np

image =cv2.imread('oggy.jpg',0)
image=cv2.resize(image,(800,700))
filter =np.array([[1,0,-1],[2,0,-2],[1,0,-1]])
result=cv2.filter2D(image,-1,filter)
cv2.imshow('Oggy Cat',result)
cv2.waitKey(0)