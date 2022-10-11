import cv2
import math
import matplotlib
import numpy as np

image = cv2.imread('hienho.jpeg',0)
image=cv2.resize(image,(800,700))
filter1 = np.array([[1,2,1],[0,0,0],[-1,-2,-1]])
result1 = cv2.filter2D(image,-1,filter1)
filter2 = np.array([[-1,-2,-1],[0,0,0],[1,2,1]])
result2=cv2.filter2D(image,-1,filter2)
cv2.imshow('AnhGoc',image)
cv2.imshow('CoNhuKhongCo1',result1)
cv2.imshow('CoNhuKhongCo2',result2)
cv2.waitKey(0)